import os
import getpass
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import ElasticsearchStore
from llama_index.storage.storage_context import StorageContext

# Connect to OpenAPI to prevent HuggingFace download
os.environ["OPENAI_API_KEY"] = "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"
import openai
openai.api_key = os.environ["OPENAI_API_KEY"]

'''
Example below for documents you want to load.
It's commented out to prevent error. src/files is untracked, 
so create that folder add your own pdf files to that folder if you want to load some files.
'''
# resume_doc = SimpleDirectoryReader(input_files=["src/files/David-Quichocho-Resume.pdf", "src/files/Mohammad Almutawa-Resume .pdf"]).load_data()

# Establish Elasticsearch connection
vector_store = ElasticsearchStore(
    index_name="resume",
    es_cloud_id="Smart_Bible:dXMtd2VzdDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQyZTgwNGMxNjAzYjA0M2E3YWJiZWU5ZGZjY2MyYmU0YSRmZGYwYzY4OGYxMjA0MDBmYWNjYzQyZTA0MWEyZWM4Yg==",
    es_api_key="cWN6SndJb0I4a2wxUUdVQ1NTWkU6cUxra2htbGdUVS1NV3VNdDZ4aHlrdw=="
)

storage_context = StorageContext.from_defaults(vector_store=vector_store)
# If actually loading documets, replace [] with the documents to load
index = VectorStoreIndex.from_documents([], storage_context=storage_context)
query_engine = index.as_query_engine()

def connectTest():
    return query_engine.query("What do Dave, Aaron, and Mohammad have in common?")