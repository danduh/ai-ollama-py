import os
import nest_asyncio
import config
import repo.pgvector
import utils.response_utils as utils
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex
import logging
import ingestion.ingest_pdf

logging.basicConfig(level=logging.INFO)

arch_engine = None
admin_engine = None
api_engine = None


def setup_document_vector_index(directory_reader, storage_context=None, show_progress=False):
    storage_context = storage_context if config.feature_flags[config.USE_VECTOR_DB] else None
    return VectorStoreIndex.from_documents(directory_reader,
                                           storage_context=storage_context,
                                           show_progress=show_progress)


def setup_query_engines():
    # to allow nested event loops
    nest_asyncio.apply()

    dest_url = os.getenv('DEST_URL', config.llm[config.LLM_URL])
    logging.info(f'Destination URL: {dest_url}')
    llm = Ollama(base_url=dest_url, model=config.llm[config.LLM_MODEL],
                 request_timeout=config.llm[config.LLM_REQUEST_TIMEOUT])
    embed_model = HuggingFaceEmbedding(model_name=config.embedding[config.EMBEDDING_PDF_MODEL])

    Settings.llm = llm
    Settings.embed_model = embed_model
    # Settings.chunk_size = config.ingestion[config.CHUNK_SIZE]
    # Settings.chunk_overlap = config.ingestion[config.CHUNK_OVERLAP]

    logging.info("indexing arch")
    arch_index = VectorStoreIndex.from_documents(ingestion.ingest_pdf.docs_arch)
    arch_query_engine = arch_index.as_query_engine(streaming=config.feature_flags[config.FEATURE_FLAGS_STREAMING],
                                                   similarity_top_k=config.engine[config.ENGINE_KNN_VAL])

    logging.info("indexing admin")
    admin_index = setup_document_vector_index(ingestion.ingest_pdf.docs_admin,
                                              storage_context=repo.pgvector.admin_storage_context,
                                              show_progress=config.feature_flags[config.SHOW_INGESTION_PROGRESS])
    admin_query_engine = admin_index.as_query_engine(streaming=config.feature_flags[config.FEATURE_FLAGS_STREAMING],
                                                     similarity_top_k=config.engine[config.ENGINE_KNN_VAL])
    logging.info("indexing api")
    api_index = VectorStoreIndex.from_documents(ingestion.ingest_pdf.docs_api)
    api_query_engine = api_index.as_query_engine(streaming=config.feature_flags[config.FEATURE_FLAGS_STREAMING],
                                                 similarity_top_k=config.engine[config.ENGINE_KNN_VAL])

    logging.info("indexing consolidated")
    consolidated_index = setup_document_vector_index(ingestion.ingest_pdf.docs_consolidated,
                                                     storage_context=repo.pgvector.consolidated_storage_context,
                                                     show_progress=config.feature_flags[config.SHOW_INGESTION_PROGRESS])
    consolidated_query_engine = consolidated_index.as_query_engine(
        streaming=config.feature_flags[config.FEATURE_FLAGS_STREAMING],
        similarity_top_k=config.engine[config.ENGINE_KNN_VAL])

    return arch_query_engine, admin_query_engine, api_query_engine, consolidated_query_engine
