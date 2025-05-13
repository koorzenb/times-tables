import pytest
import sys
import os
import json
import time
from io import StringIO
from unittest.mock import patch, MagicMock, Mock

# Import the module to test
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Times_Tables.tables import generate_question, ask_question, print_response, add_entry_to_high_scores

# Test the generate_question function
def test_generate_question():
    # Test that the function returns numbers within range
    for _ in range(100):  # Test multiple times to ensure randomness works correctly
        num1, num2, prod = generate_question(9)
        assert prod == num1 * num2
        assert 1 <= num1 <= 9
        assert 1 <= num2 <= 9

# Test the ask_question function
@pytest.mark.parametrize("question,input_value,expected", [
    ("What is 3 * 4", "12", 12),
    ("What is 5 * 6", "30", 30),
    ("What is 9 / 3", "3", 3)
])
def test_ask_question(question, input_value, expected):
    with patch('builtins.input', return_value=input_value):
        result = ask_question(question)
        assert result == expected

# Test handling invalid input
def test_ask_question_invalid_input():
    # Test that the function keeps asking until valid input is provided
    with patch('builtins.input', side_effect=["abc", "7"]):
        result = ask_question("What is 3 + 4")
        assert result == 7

# Test the print_response function
@pytest.mark.parametrize("is_correct,answer,equation,expected_output", [
    (True, 12, "3 * 4", "Correct"),
    (False, 12, "3 * 4", "Wrong")
])
def test_print_response(is_correct, answer, equation, expected_output, capsys):
    print_response(is_correct, answer, equation)
    captured = capsys.readouterr()
    assert expected_output in captured.out

# Test the main function
def test_main():
    # Mock all necessary components to isolate the main function
    with patch('builtins.input', side_effect=["Test User", "12", "30", "3"]), \
         patch('json.dump'), \
         patch('json.loads', return_value={}), \
         patch('time.time', side_effect=[0, 60]), \
         patch('os.path.exists', return_value=True), \
         patch('builtins.open', MagicMock()):
        
        # Mock random choice to always return True (multiplication)
        with patch('random.choice', return_value=True):
            # Mock generate_question to return predictable values
            with patch('Times_Tables.tables.generate_question', 
                      side_effect=[(3, 4, 12), (5, 6, 30), (3, 1, 3)]):
                main()

# Run the tests
if __name__ == "__main__":
    pytest.main(["-v"])