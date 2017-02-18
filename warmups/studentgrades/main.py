from student import Student

def main():

    student1 = Student('Ashley', 12)


    is_running = True
    while is_running == True:
        menu = input("Enter 'A' to add score. Enter 'B' to get current score. Enter 'C' to get letter grade. Enter 'D' to quit: ")
        print(menu)
        if menu == 'A':
            prompt1 = int(input("Enter new score: "))
            print(prompt1)
            student1.add_score(prompt1)

        elif menu == 'B':
            print("Student Score: {}.".format(student1.get_scores()))

        elif menu == 'C':
            print("Student Grade: {}.".format(student1.get_grade()))

        elif menu == 'D':
            is_running = False
            print("Goodbye.")
            break

main()
