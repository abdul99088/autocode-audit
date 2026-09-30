import unittest
from src.ast_parser import parse_code_to_ast

class TestHallucinationGuard(unittest.TestCase):

    def test_secure_code_no_false_positives(self):
        """Verifies AST metadata correctly grounds analysis for secure code."""
        secure_code = """
import logging
import os

def safe_function():
    key = os.getenv('SAFE_KEY')
    logging.info('Executing safely')
"""
        ast_result = parse_code_to_ast(secure_code)
        
        # Verify that safe code parsing succeeds and doesn't detect unsafe nodes like os.system
        self.assertNotIn("os.system", str(ast_result))
        self.assertEqual(ast_result["status"], "success")

if __name__ == "__main__":
    unittest.main()