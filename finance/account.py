from .transaction import Transaction  # import the Transaction class

class Account:
    def __init__(self, name):
        
        self.name = name
        self.transactions = []  # Start with no transactions yet

    def add_transaction(self, transaction):
        
        self.transactions.append(transaction)

    def get_balance(self):
       
        income = 0
        expenses = 0
        for t in self.transactions:
            if t.category == "income":
                income += t.amount
            elif t.category == "expense":
                expenses += t.amount
        return income - expenses

    def show_transactions(self):
        
        print(f"Transactions for {self.name}:")
        for t in self.transactions:
            print(t)
