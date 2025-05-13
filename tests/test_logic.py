import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.logic import *

class TestLogic(unittest.TestCase):
    def test_generate_question(self):
        num1, num2, prod = generate_question(9)
        self.assertTrue(1 <= num1 <= 9)
        self.assertTrue(1 <= num2 <= 9)
        self.assertEqual(num1 * num2, prod)
        
    def test_ask_question(self):
        pass
    
    def test_print_response(self):
        pass
