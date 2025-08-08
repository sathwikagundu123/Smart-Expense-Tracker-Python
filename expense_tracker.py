from datetime import datetime

class Expense:
    def __init__(self, category, amount, date, description):
        self.category = category
        self.amount = amount
        self.date = date
        self.description = description

    def __str__(self):
        return f"{self.date} | {self.category} | Rs.{self.amount:.2f} | {self.description}"

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def view_all_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            for exp in self.expenses:
                print(exp)

    def calculate_total(self):
        return sum(exp.amount for exp in self.expenses)

def main():
    manager = ExpenseManager()

    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenditure")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            category = input("Category: ")
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            date_input = input("Date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date_input, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue
            description = input("Description: ")
            manager.add_expense(Expense(category, amount, date_input, description))
            print("Expense added successfully!")

        elif choice == "2":
            manager.view_all_expenses()

        elif choice == "3":
            total = manager.calculate_total()
            print(f"Total Expense: Rs.{total:.2f}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
