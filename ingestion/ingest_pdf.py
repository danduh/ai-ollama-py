from llama_index.core import SimpleDirectoryReader
import config

docs_admin = SimpleDirectoryReader(input_files=[config.data[config.ADMIN_FILE_PATH]]).load_data()
docs_arch = SimpleDirectoryReader(input_files=[config.data[config.ARCH_FILE_PATH]]).load_data()
