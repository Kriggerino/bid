import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_ENV = os.environ.get("PINECONE_ENVIRONMENT")
SERPAPI_KEY = os.environ.get("SERPAPI_KEY")
CHATPDF_API_KEY = os.environ.get("CHATPDF_API_KEY")

print(OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_ENV, SERPAPI_KEY, CHATPDF_API_KEY)