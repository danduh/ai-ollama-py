import os

from llama_index.core import SimpleDirectoryReader
import config


def ingest_directory(directory_path):
    return SimpleDirectoryReader(input_dir=directory_path, recursive=True).load_data()


def ingest_files(file_list):
    return SimpleDirectoryReader(input_files=file_list).load_data()


def ingest_consolidated_files():
    consolidated_reader = ingest_directory(config.data[config.DATA_DIR]) \
        if not config.feature_flags[config.CONFIGURABLE_PATH] else\
        ingest_directory(str(os.getenv("INGEST_DIR")))
    return consolidated_reader

docs_consolidated = ingest_consolidated_files()
