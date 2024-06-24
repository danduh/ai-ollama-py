import nest_asyncio
import config
import utils.response_utils as utils
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex

import ingestion.ingest_pdf

arch_engine = None
admin_engine = None


def setup_query_engines():
    # to allow nested event loops
    nest_asyncio.apply()

    llm = Ollama(model=config.llm[config.LLM_MODEL], request_timeout=config.llm[config.LLM_REQUEST_TIMEOUT])
    embed_model = HuggingFaceEmbedding(model_name=config.embedding[config.EMBEDDING_PDF_MODEL])
    Settings.llm = llm
    Settings.embed_model = embed_model

    # response = llm.complete("tell me about powerflex")
    # print(response)

    arch_index = VectorStoreIndex.from_documents(ingestion.ingest_pdf.docs_arch)
    arch_query_engine = arch_index.as_query_engine(streaming=config.feature_flags[config.FEATURE_FLAGS_STREAMING],
                                                   similarity_top_k=config.engine[config.ENGINE_KNN_VAL])

    # results = query_engine.query("Tell me about the powerflex architecture in short reference sds and components")
    # print(str(results))


    admin_index = VectorStoreIndex.from_documents(ingestion.ingest_pdf.docs_admin)
    admin_query_engine = admin_index.as_query_engine(streaming=config.feature_flags[config.FEATURE_FLAGS_STREAMING],
                                                   similarity_top_k=config.engine[config.ENGINE_KNN_VAL])

    # results = query_engine.query("As an experienced engineer who know the Powerflex system and how to use it very well, Tell me How to work with the system to consume storage, give me ateps and settings for that to use, if there are prerequisites to configure, such as other powerflex storage objects or resources, reference them too in the process, be concise and informative, and help the user understand what to do step by step")
    # results = query_engine.query("Tell me How to work with the system to consume storage, give me ateps and settings for that to use, if there are prerequisites to configure, such as other powerflex storage objects or resources, reference them too in the process")


    return arch_query_engine, admin_query_engine

def test_queries():
    if admin_engine != None:
        results = admin_engine.query("im getting an error for adding a device, what are the reasons for that")
        results.print_response_stream()
        return utils.enrich_response(results)




if __name__ == "__main__":
    arc_engine, admin_engine = setup_query_engines()
    # setup rest service
    print(test_queries())
