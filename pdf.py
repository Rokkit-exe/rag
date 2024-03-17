import os
from dotenv import load_dotenv
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader

load_dotenv()

def get_index(data, index_name):
    index = None

    if not os.path.exists(index_name):
        print(f"Creating index {index_name}...")
        index = VectorStoreIndex.from_documents(data, show_progress=True, index_name=index_name)
        index.storage_context.persist(persist_dir=index_name)

    else:
        index = load_index_from_storage(StorageContext.from_defaults(persist_dir=index_name))

    return index


pdf_path = os.path.join('data', 'Canada.pdf')

canada_pdf = PDFReader().load_data(pdf_path)

canada_index = get_index(data=canada_pdf, index_name='canada')
canada_engine = canada_index.as_query_engine()

