import sys
from src.ast_parser import parse_code_to_ast
from src.security_agent import analyze_ast_vulnerabilities

sample_code = """
import os

def check_user(user_input):
    api_key = "12345-SECRET-KEY"
    os.system(f"echo Checking {user_input}")
"""

print("=== Running AST Parser (SCRUM-18) ===")
ast_result = parse_code_to_ast(sample_code)
print("AST Analysis Result:", ast_result)
sys.stdout.flush()

print("\n=== Running Gemini Security Agent Node (SCRUM-19) ===")
print("Querying Gemini 3.6 Flash model... please wait...")
sys.stdout.flush()

analysis = analyze_ast_vulnerabilities(sample_code, ast_result)

print("\n--- Security Agent Final Output ---")
print(analysis)
sys.stdout.flush()