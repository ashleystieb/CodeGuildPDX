def math_quiz():
    questions = {"10 / 2 = ":5, "20 / 5 = ":4, "40 / 4 = ":10, "100 / 5 = ":20, "60 / 4 = ":15}
    correct = 0
    wrong = 0
    questions.items()
    for key,value in questions.items():
        question = int(input(key))
        if question == value:
            correct += 1
            print("Correct.")
        else:
            wrong += 1
            print("Incorrect.")
    print(("You got {} correct and {} wrong.").format(correct,wrong))

def main():
    math_quiz()

main()
