import ast

def parse_code_to_ast(code_snippet: str):
    """Parses raw Python code into an AST node structure."""
    try:
        parsed_ast = ast.parse(code_snippet)
        functions = [node.name for node in ast.walk(parsed_ast) if isinstance(node, ast.FunctionDef)]
        imports = [node.names[0].name for node in ast.walk(parsed_ast) if isinstance(node, ast.Import)]
        return {
            "status": "success",
            "functions_found": functions,
            "imports_found": imports,
            "ast_tree": parsed_ast
        }
    except SyntaxError as e:
        return {"status": "error", "message": str(e)}