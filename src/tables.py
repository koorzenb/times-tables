import json
import os
import time
import sys
from config import NUMBER_OF_QUESTIONS

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Now we can import logos and logic modules
from logos import welcome, congratulations, try_next_time
from logic import *

# def waiting_for_answer():
#     threading.Event().wait(2)
#     print("Time's up!")

def get_high_scores():
    file = os.path.join(os.path.dirname(__file__), "high_scores.json")
    if not os.path.exists(file):
        with open(file, "w") as data_file:
            json.dump({}, data_file)
            return None
    else:
        with open(file, "r") as data_file:
            str_data = data_file.read()
            if str_data:
                high_scores = json.loads(str_data)
                return high_scores
            else:
                return {}

def show_high_scores(high_scores = None):
    if high_scores is None:
        high_scores = get_high_scores()
  
    print("\nHigh Scores:")
    for user, record in high_scores.items():
        print(f"- {user.title()}: {record['time']} seconds")

    print("\n")
    
def main():
    print('\n' * 20)
    print(f"{welcome}\n")

    show_high_scores()
    
    name = input("Enter your name: ")
    name = name.lower()
    correct_answers = 0
    index = 1

    starting_time = time.time()

    for _ in range(NUMBER_OF_QUESTIONS):
        num1, num2, prod = generate_question(9)
        is_multiply = random.choice([True, False])

        if is_multiply:
            eq = f"{num1} * {num2}"
            answer = prod
        else:
            eq = f"{prod} / {num2}"
            answer = num1

        guess = ask_question(f"{index}: What is {eq}")
        print_response(guess == answer, answer, eq)
        if guess == answer:
            correct_answers += 1

        index += 1

    print('\n' * 20)
    passed = float(correct_answers / NUMBER_OF_QUESTIONS) >= 0.8
    end_time = time.time()
    elapsed_time = end_time - starting_time
    updated_high_scores = get_high_scores()

    if passed:
        print(f"{congratulations}\n")
        print(f"{name}, you passed!")
        updated_high_scores = add_high_scores(get_high_scores(), name, correct_answers, elapsed_time)
    else:
        print(f"{try_next_time}\n")
        print(f"Sorry, {name}, you failed this time. Better luck next time!")
        
    elapsed_time = "{:.2f}".format(elapsed_time)
    print(f"You got {correct_answers} out of {NUMBER_OF_QUESTIONS} questions correct in {elapsed_time} seconds.")


    with open(os.path.join(os.path.dirname(__file__), "high_scores.json"), "w") as data_file:
        json.dump(updated_high_scores, data_file)
        show_high_scores(updated_high_scores)









if __name__ == "__main__":
    main()

 # wait on Enter before closing the console
    input("Press Enter to exit...")

