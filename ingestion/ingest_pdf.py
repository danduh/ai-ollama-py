from llama_index.core import SimpleDirectoryReader
from os import path
import config


def ingest_directory(directory_path):
    return SimpleDirectoryReader(input_dir=directory_path, recursive=True).load_data()

def ingest_files(file_list):
    return SimpleDirectoryReader(input_files=file_list).load_data()

docs_admin = ingest_files([config.data[config.ADMIN_FILE_PATH]])
docs_arch = ingest_files([config.data[config.ARCH_FILE_PATH]])
docs_api = ingest_files([config.data[config.API_FILE_PATH]])
docs_consolidated = ingest_directory(config.data[config.DATA_DIR])
