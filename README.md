Personal Finance Manager
Overview
Personal Finance Manager is a Python-based command-line application for tracking financial transactions. Users can create an account, add income and expense transactions interactively, view all transactions, and check their account balance.
Features

Create transactions with amount, category (income/expense), description, and date.
Manage transactions in an account and calculate the balance (income minus expenses).
Interactive input for adding transactions via the command line.
Input validation to ensure positive amounts and valid categories.

Project Structure
Personal_Finance_Manager/
├── finance/
│   ├── __init__.py        # Marks finance as a Python package
│   ├── account.py         # Defines the Account class to manage transactions
│   ├── transaction.py     # Defines the Transaction class for individual transactions
├── main.py                # Main script for user interaction
├── README.md              # Project documentation (this file)

Prerequisites

Python 3.8 or higher
uv (Python package and project manager)
Git

Setup Instructions

Clone or Fork the Repository:

To fork:
Visit this repository on GitHub.
Click the Fork button (top-right) to create a copy in your GitHub account.
Clone your forked repository:git clone https://github.com/your-username/Personal_Finance_Manager.git
cd Personal_Finance_Manager




To clone directly:git clone https://github.com/your-username/Personal_Finance_Manager.git
cd Personal_Finance_Manager




Set Up the Environment with uv:

Install uv if not already installed (installation guide).
Create and activate a virtual environment:uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate


Note: No external dependencies are required for this project.




Run the Application:

Run main.py as a module to avoid import errors:uv run python -m finance.main


Follow the prompts to:
Enter a transaction amount (positive number, or 0 to finish).
Specify the category (income or expense).
Provide a description.


Example output:Enter transaction amount (or 0 to finish): 1000
Enter transaction category (income/expense): income
Enter transaction description: Salary
Enter transaction amount (or 0 to finish): 200
Enter transaction category (income/expense): expense
Enter transaction description: Groceries
Enter transaction amount (or 0 to finish): 0

Transactions for My Main Account:
2025-06-10 21:42:00 | Salary | income | 1000.00
2025-06-10 21:42:10 | Groceries | expense | 200.00

Current balance: $800.00





Forking and Contributing

Fork the Repository:

Fork this repository on GitHub (see Setup Instructions).
Make changes in your fork (e.g., add features, fix bugs).


Submit a Pull Request:

Commit and push your changes:git add .
git commit -m "Describe your changes"
git push origin main


In your forked repository on GitHub, click Contribute > Open pull request.
Submit the pull request to the original repository (your-username/Personal_Finance_Manager).



Notes

The finance directory is a Python package (due to __init__.py). Always run main.py as a module (uv run python -m finance.main) to avoid ImportError issues with relative imports in account.py.
Use uv to manage the Python environment for consistency.

License
This project is unlicensed. Feel free to use and modify it as needed.






^G Get Help       ^O WriteOut       ^R Read File      ^Y Prev Pg        ^K Cut Text       ^C Cur Pos        
^X Exit           ^J Justify        ^W Where is       ^V Next Pg        ^U UnCut Text     ^T To Spell # Personal_Finance_Manager
a Python-based application for tracking income, expenses, budgets, and financial reports.
