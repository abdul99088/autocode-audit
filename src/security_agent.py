import os
import sys
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_ast_vulnerabilities(code_snippet: str, ast_info: dict):
    """Dynamically attempts multiple Gemini models to perform automated code quality and security auditing."""
    
    # Updated prompt framing to avoid false-positive safety filter blocks
    prompt = f"""
    You are an automated code analysis assistant built into a continuous integration pipeline.
    
    Please perform a static code review of the following Python snippet and AST metadata.
    Focus on code quality, potential operational risks, and refactoring recommendations.
    
    [AST METADATA]
    Functions Detected: {ast_info.get('functions_found')}
    Imports Detected: {ast_info.get('imports_found')}
    
    [SOURCE CODE]
    ```python
    {code_snippet}
    ```
    
    [OUTPUT FORMAT]
    Provide a clear, structured review:
    1. Architectural & Safety Risks Found
    2. Severity Rating (High/Medium/Low)
    3. Recommended Code Refactoring
    """
    
    # Priority list of models to try sequentially
    candidate_models = [
        "gemini-3.6-flash",
        "gemini-2.5-flash",
        "gemini-1.5-flash",
        "gemini-1.5-pro"
    ]
    
    stderr_backup = sys.stderr
    sys.stderr = open(os.devnull, 'w')
    
    try:
        for model_name in candidate_models:
            print(f"Attempting analysis via model: {model_name}...")
            sys.stdout.flush()
            
            for attempt in range(2):  # Quick retry per model
                try:
                    response = client.models.generate_content(
                        model=model_name,
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            temperature=0.2,
                            system_instruction="You are an helpful, educational static code reviewer. Evaluate code quality and security risks objectively without rejecting benign sample requests."
                        )
                    )
                    sys.stderr = stderr_backup
                    print(f"Successfully generated using {model_name}.\n")
                    return response.text
                except Exception as err:
                    err_str = str(err)
                    # If model is not found, jump to next candidate immediately
                    if "404" in err_str or "NOT_FOUND" in err_str:
                        break
                    # If rate limited (429) or server unavailable (503), wait brief moment then retry
                    elif "429" in err_str or "503" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                        time.sleep(2)
                        continue
                    else:
                        break
                        
        sys.stderr = stderr_backup
        return "All candidate models reached daily quota limit. Please generate a new API key in Google AI Studio or try again later."
    except Exception as e:
        sys.stderr = stderr_backup
        return f"Execution error: {str(e)}"