import json

class Expense:
    def __init__(self, id, description, category, amount):
        self.id = id
        self.description = description
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"{self.id}: {self.description}, Category: {self.category}, Amount: ${self.amount}"

expenses = []
last_id = 0

def load_expenses():
    global last_id
    try:
        with open('expenses.json', 'r') as f:
            data = json.load(f)
            for item in data:
                expenses.append(Expense(**item))
            last_id = max([exp.id for exp in expenses], default=0)
    except FileNotFoundError:
        pass

def save_expenses():
    with open('expenses.json', 'w') as f:
        json.dump([exp.__dict__ for exp in expenses], f)

def add_expenses():
    global last_id
    description = input("Enter expense description: ")
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    last_id += 1
    expenses.append(Expense(last_id, description, category, amount))
    save_expenses()
    print("Expense added successfully.")

def list_expenses():
    for expense in expenses:
        print(expense)

def delete_expense():
    id_to_delete = int(input("Enter expense ID to delete: "))
    global expenses
    expenses = [exp for exp in expenses if exp.id != id_to_delete]
    save_expenses()
    print("Expense deleted successfully.")

def main():
    load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. List Expense")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expenses()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()