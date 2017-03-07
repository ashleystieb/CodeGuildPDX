

# CHECKING ACCOUNT CLASS

class Checking:

    def __init__(self, initial_deposit = None, *args, **kwargs):

        self.transactions = []

        # Logic to see if initial_deposit is provided

        if initial_deposit is None:

            self.balance = 0.0

        else:

            self.balance = float(initial_deposit)

            transaction_message = "Initial Deposit {} into Checking".format(initial_deposit)

            self.transactions.append(transaction_message)



    def deposit(self, amount):

        self.balance += amount

        transaction_message = "Deposited {} into Checking".format(amount)

        # Other way to create message using string concatenation
        # transaction_message = "Deposited " + str(amount) + " into Checking"

        self.transactions.append(transaction_message)

    def withdrawal(self,amount):
        self.balance -= amount

        transaction_message = "Withdrew {} from Checking".format(amount)

        self.transactions.append(transaction_message)

    def get_balance(self):

        return self.balance

    def get_transaction_history(self):

        return self.transactions


    def transfer(self,amount):

        self.balance -= amount

        transaction_message = "Transferred {} to Savings".format(amount)

        self.transactions.append(transaction_message)


    def receive_transfer(self,amount):

        self.balance += amount

        transaction_message = "Received ${} Transfer from Savings".format(amount)

        self.transactions.append(transaction_message)

# SAVINGS ACCOUNT CLASS


class Savings:

    def __init__(self, interest_rate = 0.05, *args, **kwargs):
        self.balance = 0.0
        self.transactions = []
        self.interest_rate = interest_rate






    def apply_interest(self):
        interest_accrued = (self.balance * self.interest_rate)
        self.balance += interest_accrued

        transaction_message = "Interest Deposit {} into Savings".format(interest_accrued)

        self.transactions.append(transaction_message)


    def deposit(self, amount):

        self.balance += amount

        transaction_message = "Deposited {} into Checking".format(amount)

        # Other way to create message using string concatenation
        # transaction_message = "Deposited " + str(amount) + " into Checking"

        self.transactions.append(transaction_message)

    def withdrawal(self,amount):
        self.balance -= amount

        transaction_message = "Withdrew {} from Checking".format(amount)

        self.transactions.append(transaction_message)


    def get_balance(self):

        return self.balance


    def transfer(self, amount):

        self.balance -= amount

        transaction_message = "Transferred {} to Checking".format(amount)

        self.transactions.append(transaction_message)


    def get_transaction_history(self):

        return self.transactions



    def receive_transfer(self, amount):
        self.balance += amount

        transaction_message = "Received ${} Transfer from Checking".format(amount)

        self.transactions.append(transaction_message)




class BankAccount:


    def __init__(self, id_number, initial_deposit = None, *args, **kwargs):

        self.id_number = id_number

        self.checking = Checking(initial_deposit)

        self.savings = Savings()

        self.total_deposits = 0.0

        self.total_withdrawals = 0.0

        self.total_balance = self.checking.balance + self.savings.balance

        self.transactions = []






    def deposit(self,amount,account):

        if account == 'checking':

            self.checking.deposit(amount)

            self.total_deposits += amount

            self.total_balance += amount

            transaction_message = "Deposited ${} into Checking".format(amount)


        else:

            self.savings.deposit(amount)

            self.total_deposits += amount

            self.total_balance += amount

            transaction_message = "Deposited ${} into Savings".format(amount)


        self.transactions.append(transaction_message)



    def withdrawal(self, amount, account):

        if account == 'checking':

            self.checking.withdrawal(amount)

            self.total_withdrawals += amount

            self.total_balance -= amount

            transaction_message = "Withdrew ${} from Checking".format(amount)


        else:

            self.savings.withdrawal(amount)

            self.total_withdrawals += amount

            self.total_balance -= amount

            transaction_message = "Withdrew ${} from savings".format(amount)


        self.transactions.append(transaction_message)


    def transfer(self, account_from, amount):


        if account_from == 'checking':

            # Transfer from checking to savings

            self.checking.transfer(amount)

            self.savings.receive_transfer(amount)

            transaction_message = "Transferred ${} from Checking into Savings".format(amount)

        else:

            # Transfer from savings to checking

            self.savings.transfer(amount)

            self.checking.receive_transfer(amount)

            transaction_message = "Transferred ${} from Savings into Checking".format(amount)


        self.transactions.append(transaction_message)



    def get_balance(self):

        return self.total_balance


    def get_transaction_history(self):

        return self.transactions



    def __str__(self):

        # member idnum has a total balance of balance

        returnVal = "member {} has a total balance of {}".format(self.id_number, self.total_balance)

        return returnVal






class Bank:

    def __init__(self, name):

        self.name = name

        self.member_size = 0

        self.members = []

        self.total_worth = 0.0



    def create_account(self,id_num, initial_deposit = None):

        temp_account = BankAccount(id_num, initial_deposit)

        self.members.append(temp_account)

        self.member_size += 1



    def get_members(self):

        for member in self.members:

            print(member)



    def get_total_worth(self):

        for member in self.members:

            self.total_worth += member.get_balance()

        return self.total_worth


    def get_member_by_id(self,id_num):

        for i in range(0,len(self.members)):

            current_member = self.members[i]

            if current_member.id_number == id_num:

                return current_member



    def print_menu(self):

        menu =  '''
                How may I help you? Please choose one of the following.

                1) Withdraw

                2) Deposit

                3) Check Balance

                4) Transfer to Savings

                5) Transfer to Checking

                6) View Transactions

                7) Sign Out

                '''

        return menu


    def sign_in(self):

        account_num = int(input("Enter your account number "))

        member = self.get_member_by_id(account_num)

        while True:

            menu_choice = int(input(self.print_menu()))


            if menu_choice == 1:


                sub_choice = input("Withdrawal from checking or savings? ")

                amount = int(input("How much do you want to  withdrawal? "))

                member.withdrawal(amount,sub_choice)

            elif menu_choice == 2:

                sub_choice = input("Deposit to checking or savings? ")

                amount = int(input("How much do you want to  deposit? "))

                member.deposit(amount, sub_choice)

            elif menu_choice == 3:

                print("Your current balance is: ", str(member.get_balance))

            elif menu_choice == 4:

                amount = int(input("How much do you want to transfer to savings? "))

                member.transfer('checking', amount)

            elif menu_choice == 5:

                amount = int(input("How much do you want to transfer to checking? "))

                member.transfer('savings', amount)

            elif menu_choice == 6:

                print(member.transactions)

            else:

                break










































