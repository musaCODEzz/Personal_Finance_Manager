from finance.transaction import Transaction
from finance.account import Account

def main():
    account = Account("My Main Account")

    # Add transactions
    t1 = Transaction(amount=1000, category="income", description="Salary")
    t2 = Transaction(amount=200, category="expense", description="Groceries")
    t3 = Transaction(amount=150, category="expense", description="Internet")

    account.add_transaction(t1)
    account.add_transaction(t2)
    account.add_transaction(t3)

    # Show all transactions
    print(f"\nTransactions for {account.name}:")
    account.show_transactions()

    # Show balance
    print(f"\nCurrent balance: ${account.get_balance():.2f}")

if __name__ == "__main__":
    main()
