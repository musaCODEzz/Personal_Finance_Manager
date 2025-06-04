# from datetime import datetime

# class Transaction:
#     def __init__(self, amount: float, category: str, description: str = "", date: str = None):
#         if amount <= 0:
#             raise ValueError("Amount must be positive")
#         self.amount = amount
#         self.category = category
#         self.description = description
#         self.date = datetime.strptime(date, "%Y-%m-%d") if date else datetime.now()

#     def __repr__(self):
#         return f"{self.date.date()} | {self.category} | {self.amount:.2f} | {self.description}"


class Transaction:
    def __init__(self, amount, description, category):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.amount = amount
        self.description = description
        self.category = category

amount = input("Enter transaction amount: ")
description = input("Enter transaction description: ").strip().title()
category = input("Enter transaction category (income/expense): ").strip().lower()
transaction = Transaction(amount, description, category)
print(transaction.__dict__)