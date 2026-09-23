from database import add_expense, show_expense, remove_expense, update_expensedb, viewbyinc, viewbydesc, costsum, filterbyfood, filterbyshopping, filterbytransport

def save_expense():
    amount = int(input("Enter Amount: "))
    category = input("Enter Category: ")
    description = input("Description: ")

    add_expense(amount, category, description)

def delete_expense():
    userdeleteid = int(input("Which ID you want to delete: "))
    remove_expense(userdeleteid)
    
def update_expense():
    userupdateid = int(input("Which data you want to update: "))
    amtupdate = input("Update Amount: ")
    catupdate = input("Update Category: ")
    descupdate = input("Update Description: ")
    update_expensedb(userupdateid, amtupdate, catupdate, descupdate)
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Update Expense")
    print("5. Exit")

    useri = int(input("Enter choice: "))

    if useri == 1:
        print(show_expense())
        save_expense()
    elif useri == 2:
        print("\n1. View in Increasing Order")
        print("2. View in Decreasing Order")
        print("3. View Summary")
        print("4. Sort by Category")

        sort = int(input("Enter choice: "))

        if sort == 1:
            print(viewbyinc())
        elif sort == 2:
            print(viewbydesc())
        elif sort == 3:
            costsum()
        elif sort == 4:
            print("\n1. Food")
            print("2. Transport")
            print("3. Shopping")
            userifilter = int(input("Enter choise: "))
            if userifilter == 1:
                print(filterbyfood())
            elif userifilter == 2:
                print(filterbytransport())
            elif userifilter == 3:
                print(filterbyshopping())
    elif useri == 3:
        print(show_expense())
        delete_expense()
    elif useri == 4:
        print(show_expense())
        update_expense()
    elif useri == 5:
        break
    else:
        print("Invalid choice.")