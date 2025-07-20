import os

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
DATASET= os.getenv("DATASET_ID")
TABLE = os.getenv("TABLE_ID")

# Initialize Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

embedding = VertexAIEmbeddings(
    model_name="text-embedding-005",
    project=PROJECT_ID,
    location=REGION
)

vector_store = BigQueryVectorStore(
    project_id=PROJECT_ID,
    dataset_name=DATASET,
    table_name=TABLE,
    location=REGION,
    embedding=embedding,
)

def run_similarity_search(query, k=5):
    docs = vector_store.similarity_search(query, k=k)
    return docs

if __name__ == "__main__":
    # Test with the same search you provided
    search = vector_store.similarity_search("Security")
    print(f"here are the docs searched {search}")
    
    # Additional example
    query = "What are the key skills for a Google Cloud Architect?"
    results = run_similarity_search(query)
    print(f"\nQuery: {query}")
    print("Results:")
    for i, doc in enumerate(results):
        print(f"{i+1}. {doc.page_content[:200]}...")
        print("-" * 50) 