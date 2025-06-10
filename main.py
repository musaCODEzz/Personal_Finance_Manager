# from finance.transaction import Transaction
# from finance.account import Account

# def main():
#     account = Account("My Main Account")

#     # Add transactions
#     t1 = Transaction(amount=1000, category="income", description="Salary")
#     t2 = Transaction(amount=200, category="expense", description="Groceries")
#     t3 = Transaction(amount=150, category="expense", description="Internet")

#     account.add_transaction(t1)
#     account.add_transaction(t2)
#     account.add_transaction(t3)

#     # Show all transactions
#     print(f"\nTransactions for {account.name}:")
#     account.show_transactions()

#     # Show balance
#     print(f"\nCurrent balance: ${account.get_balance():.2f}")

# if __name__ == "__main__":
#     main()
from finance.transaction import Transaction
from finance.account import Account

def main():
    account = Account("My Main Account")

    # Get user input for transactions
    while True:
        try:
            amount = float(input("Enter transaction amount (or 0 to finish): "))
            if amount == 0:
                break
            if amount < 0:
                print("Amount must be positive. Try again.")
                continue
            category = input("Enter transaction category (income/expense): ").strip().lower()
            if category not in ["income", "expense"]:
                print("Category must be 'income' or 'expense'. Try again.")
                continue
            description = input("Enter transaction description: ").strip().title()

            # Create and add transaction
            transaction = Transaction(amount, category, description)
            account.add_transaction(transaction)
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")

    # Show all transactions
    print(f"\nTransactions for {account.name}:")
    account.show_transactions()

    # Show balance
    print(f"\nCurrent balance: ${account.get_balance():.2f}")

if __name__ == "__main__":
    main()