
# Engine Config Keys
ENGINE_KNN_VAL = "knn_val"

# Feature Flags Config Keys
FEATURE_FLAGS_STREAMING = "streaming"
FEATURE_FLAGS_REFERENCES = "references"

# Printers Config Keys
PRINTERS_PROMPT_END = "prompt_end"
PRINTERS_PROMPT_SEPARATOR = "prompt_separator"

# Embedding Config Keys
EMBEDDING_PDF_MODEL = "pdf_model"

# LLM Config Keys
LLM_MODEL = "model"
LLM_REQUEST_TIMEOUT = "request_timeout"

# Data Config Keys
ADMIN_FILE_PATH = "admin_file_path"
ARCH_FILE_PATH = "arch_file_path"

engine = {
    ENGINE_KNN_VAL: 3,
}

feature_flags = {
    FEATURE_FLAGS_STREAMING: True,
    FEATURE_FLAGS_REFERENCES: True,
}

printers = {
    PRINTERS_PROMPT_END: "===============",
    PRINTERS_PROMPT_SEPARATOR: "----------------",
}

embedding = {
    EMBEDDING_PDF_MODEL: "BAAI/bge-small-en-v1.5",
}

llm = {
    LLM_MODEL: "llama3",
    LLM_REQUEST_TIMEOUT: 120,
}

data = {
    ADMIN_FILE_PATH: "data/flex-rack-admin-guide-45x-en-us.pdf",
    ARCH_FILE_PATH: "data/flex-rack-archg-4x-en-us.pdf"
}