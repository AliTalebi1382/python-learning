class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} واریز شد. موجودی جدید: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("موجودی کافی نیست!")
        else:
            self.balance -= amount
            print(f"{amount} برداشت شد. موجودی جدید: {self.balance}")

    def show_balance(self):
        print(f"موجودی {self.owner}: {self.balance}")

# تست
account = BankAccount("علی", 1000)
account.show_balance()
account.deposit(500)
account.withdraw(2000)
account.withdraw(300)
account.show_balance()