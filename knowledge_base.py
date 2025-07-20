import os
import google.auth.credentials
from google.cloud import aiplatform
from langchain_google_vertexai import VertexAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_google_community import BigQueryVectorStore

from dotenv import load_dotenv

load_dotenv()

# Set up Google Cloud project
PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION")
DATASET = os.getenv("DATASET_ID")
TABLE = os.getenv("TABLE_ID")

# Initialize Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

#Embedding model
embedding = VertexAIEmbeddings(
    model_name="text-embedding-005",
    project=PROJECT_ID,
    location=REGION
)

"""
List of URLs for the certification knowledge base. This includes the study guides for the most popular cloud certifications:
1. Google Cloud Associate Cloud Engineer
2. Google Cloud Professional Cloud Security Engineer
"""

urls = [
    'https://services.google.com/fh/files/misc/associate_cloud_engineer_exam_guide_english.pdf',
    'https://services.google.com/fh/files/misc/professional_cloud_security_engineer_exam_guide_english.pdf',
]

print("Loading documents from URLs...")
#Load the documents and split them into chunks
loader = UnstructuredURLLoader(urls)
documents = loader.load()
print(f"Loaded {len(documents)} documents")

text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)
print(f"Split into {len(texts)} chunks")

for idx, split in enumerate(texts):
    split.metadata["chunk"] = idx

print("Creating BigQuery Vector Store...")
#Creating the Vector store in BigQuery
vector_store = BigQueryVectorStore(
    project_id=PROJECT_ID,
    dataset_name=DATASET,
    table_name=TABLE,
    location=REGION,
    embedding=embedding,
)

print("Adding documents to vector store...")
#Add the documents to the vector store
vector_store.add_documents(texts)
print("✅ Knowledge base created successfully!") 