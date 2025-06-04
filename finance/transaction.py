from datetime import datetime

class Transaction:
    def __init__(self, amount: float , category: str, description: str = "", date: str = None):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def __repr__(self):
        return f"{self.date} | {self.description} | {self.category} | {self.amount:.2f}"

amount = float(input("Enter transaction amount: "))
category = input("Enter transaction category (income/expense): ").strip().lower()
description = input("Enter transaction description: ").strip().title()

transaction = Transaction(amount, category, description)
print(transaction)