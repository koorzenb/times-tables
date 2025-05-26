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

def print_response(is_correct, answer, eq):
    if is_correct:
        print('\n' * 20)
        print(f"{correct}\n\n")
    else:
        print('\n')
        print(f"{wrong}\n\n {eq} = {answer}\n\n")

def add_high_scores(high_scores: Dict[str, Any], name: str, correct_answers: int, elapsed_time: float) -> Dict[str, Dict[str, Union[int, float]]]:
    passed = float(correct_answers) >= PASS_THRESHOLD

    if not passed:
        return high_scores

    user_record = high_scores.get(name, {})
    formatted_elapsed_time = "{:.2f}".format(elapsed_time)

    if not user_record:
        high_scores[name] = {"correctAnswers": correct_answers, "time": formatted_elapsed_time}
    else:
        current_correct_answers = user_record.get("correctAnswers", 0)
        current_time = user_record.get("time")
        
        if (correct_answers > current_correct_answers or 
            (elapsed_time < float(current_time) and correct_answers >= current_correct_answers)):
            print(f"New high score for {name}!")
            high_scores[name] = {"correctAnswers": correct_answers, "time": formatted_elapsed_time}
                    
    return high_scores

_username = None

def get_user_prompt(high_scores):
    usernames = list(high_scores.keys())

    # if not usernames:
    #     return "Please enter your name: "
    # else:
    prompt = "Please select a name from the list below:\n"
    for i, username in enumerate(usernames, start=1):
        prompt += f"{i}. {username.title()}\n"
    return prompt
    
def get_username(high_scores) -> str:

    # if not high_scores:
    #     username = input("Please enter your name: ").strip()
    # else:
    try:
        prompt = get_user_prompt(high_scores)
        print(prompt)
        choice = int(input())
        username = list(high_scores.keys())[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Please try again.")
        return get_username(high_scores)
    
    return username.title()
        
        
    


    