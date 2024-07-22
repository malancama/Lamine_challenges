class Account:
    def __init__(self, name, account_number, balance=2000):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def retrait(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"le retrait de {amount} a été effectué avec succés")
        else:
            print("solde insuffisant pour effectue un retrait")

    def depot(self, amount):
        self.balance += amount
        print(f"depot de {amount} a été accepté avec succés")

    def info(self):
        print(f"Account holder: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: {self.balance}")