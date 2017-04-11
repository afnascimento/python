class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        print('withdraw', self.balance)
        #return self.balance

    def deposit(self, amount):
        self.balance += amount
        print('deposit', self.balance)
        #return self.balance

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('withdraw', amount, 'Sorry, minimum balance must be maintained', self.minimum_balance)
        else:
            BankAccount.withdraw(self, amount)

print('BankAccount A')
a = BankAccount()
a.deposit(100)
a.withdraw(10)

print('BankAccount B')
b = BankAccount()
b.deposit(50)
b.withdraw(10)

print('MinimumBalanceAccount')
minimun = MinimumBalanceAccount(100)
minimun.deposit(200)
minimun.withdraw(100)
minimun.withdraw(10)