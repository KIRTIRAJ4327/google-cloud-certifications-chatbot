from langchain_community.vectorstores import MatchingEngine
from langchain_google_vertexai import VertexAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize embeddings
embeddings = VertexAIEmbeddings(
    project=os.getenv("PROJECT_ID"),
    location=os.getenv("REGION")
)

# Initialize Matching Engine vector store
vector_store = MatchingEngine(
    project_id=os.getenv("PROJECT_ID"),
    index_endpoint_id="your_index_endpoint_id",  # Replace with actual endpoint ID
    deployed_index_id="your_deployed_index_id",  # Replace with actual deployed index ID
    embedding=embeddings
)

def run_matching_engine_search(query, k=5):
    docs = vector_store.similarity_search(query, k=k)
    return docs

if __name__ == "__main__":
    query = "What are the requirements for Google Cloud Data Engineer certification?"
    results = run_matching_engine_search(query)
    print(f"Query: {query}")
    print("Results:")
    for i, doc in enumerate(results):
        print(f"{i+1}. {doc.page_content[:200]}...")
        print("-" * 50) 