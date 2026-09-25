import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_ast_vulnerabilities(code_snippet: str, ast_info: dict):
    """Sends code and AST metadata to Gemini for security analysis."""
    prompt = f"""
    You are an expert security agent in AutoCode Audit.
    Analyze the following code snippet and AST metadata for security flaws:
    
    AST Functions: {ast_info.get('functions_found')}
    AST Imports: {ast_info.get('imports_found')}
    
    Code:
    {code_snippet}
    
    Provide a concise risk assessment outlining potential vulnerabilities.
    """
    
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text