class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self, path):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    def __init__(self, filepath,fee):
        self.fee=fee
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance = self.balance - amount


account=Account("bank_account//balance.txt")
print(account.balance)
account.withdraw(250)
print(account.balance)
account.commit("bank_account//balance.txt")
