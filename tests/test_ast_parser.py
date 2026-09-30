import unittest
from src.ast_parser import parse_code_to_ast

class TestASTParser(unittest.TestCase):

    def test_valid_code_parsing(self):
        code = "import os\ndef test(): pass"
        result = parse_code_to_ast(code)
        self.assertEqual(result["status"], "success")
        self.assertIn("os", result["imports_found"])
        self.assertIn("test", result["functions_found"])

    def test_syntax_error_handling(self):
        invalid_code = "def test(:"
        result = parse_code_to_ast(invalid_code)
        self.assertEqual(result["status"], "error")

if __name__ == "__main__":
    unittest.main()