class bankaccount:
    def __init__(self, accholder, balance=0):
        self.accholder = accholder
        self._balance = balance

    def deposit(self, amount, currency=None):
        if amount > 0:
            self._balance += amount
            if currency:
                print(f"{amount} {currency} is deposited and final amount is {self._balance}")
            else:
                print(f"{amount} is deposited and final amount is {self._balance}")
        else:
            print("deposit amount is invalid")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Amount withdrawn is {amount}, balance is {self._balance}")
        else:
            print("Exceeded the limit")
        return self._balance

class savingsaccount(bankaccount):
    def __init__(self, accholder, balance=0, overdraft_limit=1000):
        super().__init__(accholder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"Amount withdrawn is {amount}, balance is {self._balance}")
        else:
            print("Exceeded the overdraft limit")
        return self._balance

basic_acc = bankaccount("MAHA", 5000)
basic_acc.deposit(12000)
basic_acc.deposit(2000, "INR")

sav_acc = savingsaccount("John", balance=3000, overdraft_limit=2000)
sav_acc.withdraw(4000)
sav_acc.withdraw(1000)
