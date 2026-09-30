import sys
from src.ast_parser import parse_code_to_ast
from src.security_agent import run_multi_agent_audit

sample_code = """
import os

def check_user(user_input):
    api_key = "12345-SECRET-KEY"
    os.system(f"echo Checking {user_input}")
"""

print("=== Running AST Parser Node (SCRUM-18) ===")
ast_result = parse_code_to_ast(sample_code)
print("AST Analysis Result:", ast_result)
sys.stdout.flush()

print("\n=== Running Multi-Agent Security Audit Pipeline (SCRUM-19) ===")
print("Executing Agent 1 (Security Review) & Agent 2 (Refactoring)... please wait...")
sys.stdout.flush()

try:
    audit_report = run_multi_agent_audit(sample_code, ast_result)
    print("\n--- Multi-Agent Audit Final Output ---")
    print(audit_report)
except Exception as e:
    print(f"\n[ERROR] Pipeline execution failed: {e}", file=sys.stderr)

sys.stdout.flush()