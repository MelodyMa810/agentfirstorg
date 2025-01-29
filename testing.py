from dotenv import load_dotenv
import os

# Load environment variables from setup.env
load_dotenv("setup.env")

# Access the environment variables
print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))
print("LangChain Tracing Enabled:", os.getenv("LANGCHAIN_TRACING_V2"))
print("LangChain API Key:", os.getenv("LANGCHAIN_API_KEY"))
print("Tavily API Key:", os.getenv("TAVILY_API_KEY"))

