import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.logic import *

class TestAddHighScores(unittest.TestCase):
    def setUp(self):
        # This method will run before each test
        self.name = "test_user"
    
    def test_add_new_entry_to_high_scores(self):
        """Test adding a new entry to high scores"""
        correct_answers = 15
        elapsed_time = '120.00'
        high_scores = {}

        updated_scores = add_high_scores(high_scores, self.name, correct_answers, float(elapsed_time))
        self.assertIn(self.name, updated_scores)
        self.assertEqual(updated_scores[self.name]["correctAnswers"], correct_answers)
        self.assertEqual(updated_scores[self.name]["time"], elapsed_time)

    def test_update_entry_with_higher_score(self):
        """Test updating an existing entry with a higher score"""
        # First create an initial entry
        
        saved_high_scores = {f"{self.name}": {"correctAnswers": 15, "time": 120.0}}

        # Then update with higher score
        correct_answers = 18
        elapsed_time = '150.00'
        updated_scores = add_high_scores(saved_high_scores, self.name, correct_answers, float(elapsed_time))
        self.assertEqual(updated_scores[self.name]["correctAnswers"], correct_answers)
        self.assertEqual(updated_scores[self.name]["time"], elapsed_time)

    def test_update_entry_with_better_time_and_lower_score(self):
        saved_correct_answers = 20
        saved_elapsed_time = '150.00'
        saved_high_scores = {f"{self.name}": {"correctAnswers": saved_correct_answers, "time": saved_elapsed_time}}
        
        correct_answers = 18
        elapsed_time = '120.00'
        updated_scores = add_high_scores(saved_high_scores, self.name, correct_answers, float(elapsed_time))
        self.assertEqual(updated_scores[self.name]["correctAnswers"], saved_correct_answers)
        self.assertEqual(updated_scores[self.name]["time"], saved_elapsed_time)
        
    def test_update_entry_with_worse_time_and_higher_score(self):
        saved_correct_answers = 20
        saved_elapsed_time = 120.0
        saved_high_scores = {f"{self.name}": {"correctAnswers": saved_correct_answers, "time": saved_elapsed_time}}
        
        correct_answers = 25
        elapsed_time = '150.00'
        updated_scores = add_high_scores(saved_high_scores, self.name, correct_answers, float(elapsed_time))
        self.assertEqual(updated_scores[self.name]["correctAnswers"], correct_answers)
        self.assertEqual(updated_scores[self.name]["time"], elapsed_time)
