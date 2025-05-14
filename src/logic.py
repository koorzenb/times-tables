import random
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logos import wrong, correct
from typing import Dict, Any, Union
from src.config import PASS_THRESHOLD

def generate_question(max_num):
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)
    return num1, num2, num1 * num2

def ask_question(text):
    try:
        return int(input(f"{text}? "))
    except ValueError:
        print('\n' * 20)
        print("Invalid input. Please enter a number.")
        return ask_question(text)

def print_response(isCorrect, answer, eq):
	if isCorrect:          
		print('\n' * 20)
		print(f"{correct}\n\n")
	else:
		print('\n')
		print(f"{wrong}\n\n {eq} = {answer}\n\n")
  
def add_high_scores(high_scores: Dict[str, Any], name: str, correct_answers: int, elapsed_time: float) -> Dict[str, Dict[str, Union[int, float]]]:
    user_record = high_scores.get(name, {})
    passed = float(correct_answers) >= PASS_THRESHOLD
    
    if not passed:
        return high_scores

    if not user_record:
        high_scores[name] = {"correctAnswers": correct_answers, "time": elapsed_time}
    else:
        current_correct_answers = user_record.get("correctAnswers", 0)
        current_time = user_record.get("time", float('inf'))
        
        if (correct_answers > current_correct_answers or 
            (elapsed_time < current_time and correct_answers >= current_correct_answers)):
            print(f"New high score for {name}!")
            high_scores[name] = {"correctAnswers": correct_answers, "time": elapsed_time}
                    
    return high_scores


