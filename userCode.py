class Wallet:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def add_money(self, amount):
        self.balance += amount


wallet = Wallet()
wallet.add_money(100)
wallet.add_money(50)
wallet.withdraw(60)
wallet.withdraw(40)
wallet.withdraw(60)

assert wallet.balance == 50

wallet2 = Wallet()
wallet2.withdraw(10)

assert wallet2.balance == 0

wallet3 = Wallet()
wallet3.add_money(1000)
wallet3.withdraw(500)
wallet3.add_money(200)
wallet3.add_money(300)

assert wallet3.balance == 1000

wallet4 = Wallet()
wallet4.add_money(500)
wallet4.withdraw(600)

assert wallet4.balance == 500

wallet5 = Wallet()
wallet5.add_money(100)
wallet5.withdraw(50)
wallet5.withdraw(25)

assert wallet5.balance == 25

print("All tests passed!")