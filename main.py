from database import add_expense
from database import show_expense, remove_expense

def save_expense():
    amount = int(input("Enter Amount: "))
    category = input("Enter Category: ")
    description = input("Description: ")

    add_expense(amount, category, description)
    
def view_expense():
    print(show_expense())

def delete_expense():
    userdeleteid = int(input("Which ID you want to delete: "))
    remove_expense(userdeleteid)
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    useri = int(input("Enter choice: "))

    if useri == 1:
        save_expense()
    elif useri == 2:
        view_expense()
    elif useri == 3:
        delete_expense()
    elif useri == 4:
        break
    else:
        print("Invalid choice.")