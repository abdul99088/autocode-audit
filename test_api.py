import os
from google import genai
from dotenv import load_dotenv

# Load API Key from environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not found in .env file.")

# Initialize the GenAI client
client = genai.Client(api_key=api_key)

# Query using the active model
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Hello! Verify connection for AutoCode Audit agent."
)

print("--- Google AI API Connection Test ---")
print("Response:", response.text)