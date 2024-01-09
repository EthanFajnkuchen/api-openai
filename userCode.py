class Wallet:
    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def delete_wallet(self):
        self.balance = 0

# Unit tests
wallet = Wallet()
wallet.add_money(100)
assert wallet.balance == 100

wallet.withdraw(50)
assert wallet.balance == 50

wallet.add_money(200)
assert wallet.balance == 250

wallet.delete_wallet()
assert wallet.balance == 0

wallet.add_money(500)
wallet.withdraw(600)
assert wallet.balance == 500

print("All unit tests passed")