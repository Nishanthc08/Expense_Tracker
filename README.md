This program is an expense tracker application implemented in Python. It allows users to perform the following operations:

    1. Add Expense: Users can add new expenses by providing a description, category, and amount.
    2. List Expense: Users can view a list of all expenses along with their details.
    3. Delete Expense: Users can delete an expense by specifying its ID.
    4. Exit: Users can exit the program when they're done managing their expenses.

Concepts Covered:

    1. File Handling (JSON): The program reads and writes expense data to a JSON file (expenses.json) for persistence across sessions.
    2. Classes and Objects: The Expense class is used to represent individual expenses, demonstrating object-oriented programming concepts.
    3. User Input/Output: The program interacts with users through the console, prompting them for input and displaying information.
    4. Global Variables: Global variables are used to maintain state across functions (expenses, last_id).
    5. Error Handling: The program handles the case where the JSON file is not found (FileNotFoundError) by ignoring the exception.
    6. Functionality Decomposition: The program is divided into functions for adding, listing, and deleting expenses to improve readability and maintainability.
    7. JSON Serialization/Deserialization: The json module is used to convert expense objects to JSON format for writing to the file (json.dump()) and to convert JSON data

