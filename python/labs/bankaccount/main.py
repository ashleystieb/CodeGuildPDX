from bank import CheckingAccount

id_1 = CheckingAccount("Jane", "Doe")

def main():
    is_running = True
    while is_running == True:
        menu = input("Hello {} {}. Pick one of the following: (1) Make a deposit. (2) Withdraw money. (3) Check balance. (4) View Transactions. (5) Quit. ".format(id_1.first_name,id_1.last_name))
        print(menu)

        if menu == '1':
            deposit_amount = int(input("Enter the amount you would like to deposit: "))
            print(deposit_amount)
            id_1.deposit_money(deposit_amount)

        elif menu == '2':
            withdrawal_amount = int(input("Enter the amount you would like to withdraw: "))
            print(withdrawal_amount)
            id_1.make_withdrawal(withdrawal_amount)


        elif menu == '3':
            print(id_1.get_balance())

        elif menu == '4':
            print(id_1.get_transaction_history())

        elif menu == '5':
            is_running = False
            print("Goodbye {} {}. Your total deposits for this session were ${} and your total withdrawals for this session were ${}. The final balance in your account is ${}.".format(id_1.first_name, id_1.last_name, id_1.deposit_total, id_1.withdrawal_total, id_1.balance))
            break

main()