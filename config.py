
# Engine Config Keys
ENGINE_KNN_VAL = "knn_val"

# Feature Flags Config Keys
FEATURE_FLAGS_STREAMING = "streaming"
FEATURE_FLAGS_REFERENCES = "references"
SHOW_INGESTION_PROGRESS = "show_ingestion_progress"
USE_VECTOR_DB = "use_vector_db"

# Printers Config Keys
PRINTERS_PROMPT_END = "prompt_end"
PRINTERS_PROMPT_SEPARATOR = "prompt_separator"

# Embedding Config Keys
EMBEDDING_PDF_MODEL = "pdf_model"

# LLM Config Keys
LLM_MODEL = "model"
LLM_REQUEST_TIMEOUT = "request_timeout"
LLM_URL = "llm_url"
LLM_PORT = "llm_port"

# Data Config Keys
DATA_DIR = "data_dir"
ADMIN_FILE_PATH = "admin_file_path"
ARCH_FILE_PATH = "arch_file_path"
API_FILE_PATH = "api_file_path"

# Server Config Keys
DEFAULT_LLM_HOST = "default_host"
DEBUG = "debug"
PORT = "port"

# Ingestion Config Keys
CHUNK_SIZE = "chunk_size"
CHUNK_OVERLAP = "chunk_overlap"

# DB Config Keys
DB_URL = "db_url"
DB_NAME = "db_name"
ADMIN_TABLE_NAME = "admin_table_name"
CONSOLIDATED_TABLE_NAME = "consolidated_table_name"


engine = {
    ENGINE_KNN_VAL: 3,
}

feature_flags = {
    FEATURE_FLAGS_STREAMING: False,
    FEATURE_FLAGS_REFERENCES: True,
    SHOW_INGESTION_PROGRESS: True,
    USE_VECTOR_DB: True,

}

printers = {
    PRINTERS_PROMPT_END: "===============\n",
    PRINTERS_PROMPT_SEPARATOR: "----------------",
}

embedding = {
    EMBEDDING_PDF_MODEL: "BAAI/bge-small-en-v1.5",
}

llm = {
    LLM_MODEL: "llama3",
    # LLM_MODEL: "pfmp-sage",
    LLM_REQUEST_TIMEOUT: 1200,
    LLM_URL: "http://0.0.0.0:11434",
    LLM_PORT: "11434",
}

data = {
    DATA_DIR: "data/",
    ADMIN_FILE_PATH: "data/flex-rack-admin-guide-45x-en-us.pdf",
    ARCH_FILE_PATH: "data/flex-rack-archg-4x-en-us.pdf",
    API_FILE_PATH: "data/h19515-powerflex-automation-with-rest-api.pdf"
}

server ={
    DEFAULT_LLM_HOST: "0.0.0.0",
    DEBUG: True,
    PORT: 8087,
}

ingestion ={
    CHUNK_SIZE: 1024,
    CHUNK_OVERLAP: 50,
}

db ={
    DB_URL: "postgresql://postgres:postgres@0.0.0.0:5432",
    DB_NAME: "vector_db",
    ADMIN_TABLE_NAME: "admin_data",
    CONSOLIDATED_TABLE_NAME: "consolidated_data"
}
