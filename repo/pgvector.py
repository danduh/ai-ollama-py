import os

import config
import constants
from sqlalchemy import make_url
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.core import StorageContext


url = make_url(os.getenv("DATABASE_URL", config.db[config.DB_URL]))
def get_vector_store(table_name: str) -> PGVectorStore:
    return PGVectorStore.from_params(
        database=config.db[config.DB_NAME],
        host=url.host,
        password=url.password,
        port=url.port,
        user=url.username,
        table_name=table_name,
        embed_dim=constants.BGE_EMBED_DIM,
    )

admin_storage_context = StorageContext.from_defaults(vector_store=get_vector_store(config.db[config.ADMIN_TABLE_NAME]))
consolidated_storage_context = StorageContext.from_defaults(vector_store=get_vector_store(config.db[config.CONSOLIDATED_TABLE_NAME]))