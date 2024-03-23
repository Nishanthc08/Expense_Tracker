import json

# Define a class to represent an expense
class Expense:
    def __init__(self, id, description, category, amount):
        self.id = id
        self.description = description
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"{self.id}: {self.description}, Category: {self.category}, Amount: ${self.amount}"

# List to store expense objects
expenses = []
# Variable to track the last ID used for an expense
last_id = 0

# Function to load expenses from a JSON file
def load_expenses():
    global last_id
    try:
        with open('expenses.json', 'r') as f:
            # Load data from JSON file
            data = json.load(f)
            # Iterate over each item in data and create Expense objects
            for item in data:
                expenses.append(Expense(**item))
            # Update last_id with the maximum expense ID
            last_id = max([exp.id for exp in expenses], default=0)
    except FileNotFoundError:
        # If the file is not found, do nothing
        pass

# Function to save expenses to a JSON file
def save_expenses():
    with open('expenses.json', 'w') as f:
        # Convert expense objects to dictionaries and save to JSON file
        json.dump([exp.__dict__ for exp in expenses], f)

# Function to add a new expense
def add_expenses():
    global last_id
    # Prompt user to enter expense details
    description = input("Enter expense description: ")
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    # Increment last_id and create a new Expense object
    last_id += 1
    expenses.append(Expense(last_id, description, category, amount))
    # Save expenses to JSON file
    save_expenses()
    print("Expense added successfully.")

# Function to list all expenses
def list_expenses():
    for expense in expenses:
        print(expense)

# Function to delete an expense by ID
def delete_expense():
    id_to_delete = int(input("Enter expense ID to delete: "))
    # Filter out the expense with the given ID
    global expenses
    expenses = [exp for exp in expenses if exp.id != id_to_delete]
    # Save expenses to JSON file
    save_expenses()
    print("Expense deleted successfully.")

# Main function to run the expense tracker program
def main():
    # Load expenses from JSON file
    load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. List Expense")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expenses()  # Add a new expense
        elif choice == "2":
            list_expenses()  # List all expenses
        elif choice == "3":
            delete_expense()  # Delete an expense
        elif choice == "4":
            print("Exiting program.")
            break  # Exit the program
        else:
            print("Invalid choice. Please try again.")  # Inform the user of an invalid choice

# Entry point of the script
if __name__ == "__main__":
    main()
