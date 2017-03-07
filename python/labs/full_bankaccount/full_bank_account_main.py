



from account_classes import Checking, Savings, BankAccount, Bank




def print_menu():

    menu = '''

            1) Open a new account

            2) Sign into an account

            3) See a list of members

            4) See our total worth

            5) Leave


           '''

    return menu


def main():

    bank = Bank("PDX Bank")

    bank.create_account(1111,1000)
    bank.create_account(2222, 2000)
    bank.create_account(3333, 3000)
    bank.create_account(4444, 4000)

    welcome = "Welcome to {} how may I help you? ".format(bank.name)

    print(welcome)

    while True:

        menu_choice = int(input(print_menu()))

        if menu_choice == 1:

            # open a new account

            id_num = int(input("Choose an ID number "))

            bank.create_account(id_num)

        elif menu_choice == 2:

            # sign in

            bank.sign_in()

        elif menu_choice == 3:

            # print members

            bank.get_members()

        elif menu_choice == 4:

            # total worth


            print("Our total worth is: ", str(bank.get_total_worth()))

        else:

            print("Thank you have a nice day")
            break


main()