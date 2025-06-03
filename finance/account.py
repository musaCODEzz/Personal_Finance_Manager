from .transaction import Transaction

class Account:
    def __init__(self, name: str):
        self.name = name
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        income = sum(t.amount for t in self.transactions if t.category == "income")
        expenses = sum(t.amount for t in self.transactions if t.category == "expense")
        return income - expenses

    def show_transactions(self):
        for t in self.transactions:
            print(t)
