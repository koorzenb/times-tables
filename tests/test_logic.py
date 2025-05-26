import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.logic import *
import pytest

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

    def test_update_entry_with_better_score_and_better_time(self):
        """Test updating an existing entry with a higher score"""
        correct_answers = 20
        elapsed_time = '120.00'
        saved_high_scores = {f"{self.name}": {"correctAnswers": correct_answers, "time": float(elapsed_time)}}

        # Then update with higher score
        correct_answers = 21
        elapsed_time = '110.00'
        updated_scores = add_high_scores(saved_high_scores, self.name, correct_answers, float(elapsed_time))
        self.assertEqual(updated_scores[self.name]["correctAnswers"], correct_answers, "Score takes preference and should be updated to the new higher score")
        self.assertEqual(updated_scores[self.name]["time"], elapsed_time, "Time should be updated")

    def test_update_entry_with_worse_score_and_better_time(self):
        saved_correct_answers = 20
        saved_elapsed_time = '120.00'
        saved_high_scores = {f"{self.name}": {"correctAnswers": saved_correct_answers, "time": saved_elapsed_time}}
        
        correct_answers = 19
        elapsed_time = '110.00'
        updated_scores = add_high_scores(saved_high_scores, self.name, correct_answers, float(elapsed_time))
        self.assertEqual(updated_scores[self.name]["correctAnswers"], saved_correct_answers, "Score should not be updated as it is worse than the saved score")
        self.assertEqual(updated_scores[self.name]["time"], saved_elapsed_time, "Time should not be updated for a worse score")
        
    def test_update_entry_with_better_score_and_worse_time(self):
        saved_correct_answers = 20
        saved_elapsed_time = 120.0
        saved_high_scores = {f"{self.name}": {"correctAnswers": saved_correct_answers, "time": saved_elapsed_time}}
        
        correct_answers = 21
        elapsed_time = '130.00'
        updated_scores = add_high_scores(saved_high_scores, self.name, correct_answers, float(elapsed_time))
        self.assertEqual(updated_scores[self.name]["correctAnswers"], correct_answers, "Score should be updated to the new higher score")
        self.assertEqual(updated_scores[self.name]["time"], elapsed_time, "Time should be updated even if it is worse than the saved time, as the score is better")

    def test_update_entry_with_worse_score_and_worse_time(self):
        saved_correct_answers = 20
        saved_elapsed_time = 120.0
        saved_high_scores = {f"{self.name}": {"correctAnswers": saved_correct_answers, "time": saved_elapsed_time}}

        correct_answers = 19
        elapsed_time = '130.00'
        updated_scores = add_high_scores(saved_high_scores, self.name, correct_answers, float(elapsed_time))
        self.assertEqual(updated_scores[self.name]["correctAnswers"], saved_correct_answers, "Score should not be updated as it is worse than the saved score")
        self.assertEqual(updated_scores[self.name]["time"], saved_elapsed_time, "Time should not be updated for a worse score")



# Add new group of tests for get_username
class TestGetUsername(unittest.TestCase):
    def setUp(self):
        self.high_scores = {
            "user1": {"correctAnswers": 10, "time": 120.0},
            "user2": {"correctAnswers": 15, "time": 90.0},
            "user3": {"correctAnswers": 20, "time": 60.0}
        }

    #  write a TDD test for get_username. The first case should be where there are no high scores and the expected prompt is to ask for a name
    @pytest.mark.skip(reason="Need to develop more logic for empty list scenario")
    def test_get_username_no_high_scores(self):
        self.high_scores = {}
        expected_prompt = "Please enter your name: "
        
        user_prompt = get_user_prompt(self.high_scores)
        self.assertEqual(user_prompt, expected_prompt)
            
    def test_get_username_with_high_scores(self):
        # The expected prompt should have header with "Please select a name from the list below" followed by the names in the high scores list. Each name should be prefixed with the index number as it occurs in the list
        expected_prompt = "Please select a name from the list below:\n1. user1\n2. user2\n3. user3\n"
        user_prompt = get_user_prompt(self.high_scores)
        self.assertEqual(user_prompt, expected_prompt)
        
    
                