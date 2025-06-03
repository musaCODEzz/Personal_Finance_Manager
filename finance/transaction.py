from datetime import datetime

class Transaction:
    def __init__(self, amount: float, category: str, description: str = "", date: str = None):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.strptime(date, "%Y-%m-%d") if date else datetime.now()

    def __repr__(self):
        return f"{self.date.date()} | {self.category} | {self.amount:.2f} | {self.description}"
