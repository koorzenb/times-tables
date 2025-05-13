import json
import os
import random
import time

from logos import *
from logic import *

NUMBER_OF_QUESTIONS = 20
# def waiting_for_answer():
#     threading.Event().wait(2)
#     print("Time's up!")


def main():
    print('\n' * 20)
    print(f"{welcome}\n")

    name = input("Enter your name: ")
    name = name.lower()
    correct_answers = 0

    index = 1

    starting_time = time.time()

    for _ in range(NUMBER_OF_QUESTIONS):
        num1, num2, prod = generate_question(9)
        isMultiply = random.choice([True, False])
        eq = ''

        if isMultiply:
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
    elapsed_time = "{:.2f}".format(elapsed_time)

    if passed:
        print(f"{congratulations}\n")
        print(f"{name}, you passed!")
    else:
        print(f"{try_next_time}\n")
        print(f"Sorry, {name}, you failed this time. Better luck next time!")
    print(f"You got {correct_answers} out of {NUMBER_OF_QUESTIONS} questions correct.")

    high_scores = {}
    file = os.path.join(os.path.dirname(__file__), "high_scores.json")

    #check if file exists
    if not os.path.exists(file):
        with open(file, "w") as data_file:
            json.dump(high_scores, data_file)

    else:
        with open(file, "r") as data_file:
            str_data = data_file.read()
            if str_data:
                high_scores = json.loads(str_data)
                user_high_record = high_scores.get(name, [])
                add_entry_to_high_scores(high_scores, name, correct_answers, elapsed_time)
            else:
                high_scores[name] = correct_answers
                print(f"New high score for {name}!")

            print("\nHigh Scores:")
            for user, record in high_scores.items():
                print(f"{user.title()}: {record['time']} seconds")

            print("\n")


    with open(file, "w") as data_file:
        json.dump(high_scores, data_file)









if __name__ == "__main__":
    main()

 # wait on Enter before closing the console
    input("Press Enter to exit...")

