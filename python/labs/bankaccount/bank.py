class CheckingAccount:

    def __init__(self, first_name, last_name, *args, **kwargs):

        self.first_name = first_name
        self.last_name = last_name
        self.transaction_history = []
        self.withdrawal_total = 0
        self.deposit_total = 0

        if len(args) == 0:
            self.balance = 0.0
        else:
            self.balance = args[0]

    def deposit_money(self, deposit_amount):
        self.balance += deposit_amount
        self.deposit_total += deposit_amount
        message_1 = "Deposited {} dollars.".format(deposit_amount)
        self.transaction_history.append(message_1)

    def make_withdrawal(self, withdrawal_amount):
        if withdrawal_amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= withdrawal_amount
            self.withdrawal_total += withdrawal_amount
            message_2 = "Withdrew {} dollars.".format(withdrawal_amount)
            self.transaction_history.append(message_2)

    def get_transaction_history(self):
        return self.transaction_history

    def get_withdrawal_total(self):
        return self.withdrawal_total

    def get_deposit_total(self):
        return self.deposit_total

    def get_balance(self):
        return self.balance

