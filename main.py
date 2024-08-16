import random


# agenerirebs 1dan 10mde cifrebs
def generate_problem():
    num1 = random.randint(1,10)
    num2 = random.randint(1, 10)
    return num1, num2


# amowmebs rom user sheyvanili pasuxi iyos integer
def get_user_input(prompt):
    while True:
        try:
            answer = int(input(prompt))
            return answer
        except ValueError:
            print("Please enter a valid integer.")


# amowmebs siswores
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


# ushvebs qvizs
def multiplication_quiz(num_problems=5):
    score = 0

    for _ in range(num_problems):
        num1, num2 = generate_problem()
        correct_answer = num1 * num2

        print(f"What is {num1} * {num2}?")
        user_answer = get_user_input("Your answer: ")

        if check_answer(user_answer, correct_answer):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.")

    print(f"\nYour final score is {score} out of {num_problems}.")


multiplication_quiz()

