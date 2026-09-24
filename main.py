import database as db

def save_expense():
    amount = int(input("Enter Amount: "))
    category = input("Enter Category: ")
    description = input("Description: ")

    db.add_expense(amount, category, description, db.today)

def delete_expense():
    userdeleteid = int(input("Which ID you want to delete: "))
    db.remove_expense(userdeleteid)
    
def update_expense():
    userupdateid = int(input("Which data you want to update: "))
    amtupdate = input("Update Amount: ")
    catupdate = input("Update Category: ")
    descupdate = input("Update Description: ")
    db.update_expensedb(userupdateid, amtupdate, catupdate, descupdate)
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Update Expense")
    print("5. Set Budget")
    print("6. Exit")

    useri = int(input("Enter choice: "))

    if useri == 1:
        print(db.show_expense())
        save_expense()
    elif useri == 2:
        print("\n1. View in Increasing Order")
        print("2. View in Decreasing Order")
        print("3. View Summary")
        print("4. Sort by Category")
        print("5. Sort by Date")
        print("6. Search")

        sort = int(input("Enter choice: "))

        if sort == 1:
            print(db.viewbyinc())
        elif sort == 2:
            print(db.viewbydesc())
        elif sort == 3:
            print("1. Total Spending")
            print("2. Monthly Spending")
            userspend = int(input("Enter choice: "))
            
            if userspend == 1:
                db.costsum()
            elif userspend == 2:
                spendstartmonth = int(input("Starting Month(1-12): "))
                spendendmonth = int(input("Ending Month(1-12): "))
                db.monthspend(spendstartmonth, spendendmonth)
        elif sort == 4:
            print("\n1. Food")
            print("2. Transport")
            print("3. Shopping")
            userifilter = int(input("Enter choise: "))
            if userifilter == 1:
                print(db.filterbyfood())
            elif userifilter == 2:
                print(db.filterbytransport())
            elif userifilter == 3:
                print(db.filterbyshopping())
        elif sort == 5:
            print("1. Sort by Year")
            print("2. Sort by Month")
            print("3. Sort by Date")
            
            sortdate = int(input("Enter choice: "))
            
            if sortdate == 1:
                yearstart = int(input("Starting Year: "))
                yearend = int(input("Ending Year: "))
                print(db.sortbyyear(yearstart, yearend))
            elif sortdate == 2:
                monthyearstart = int(input("Starting Year: "))
                monthyearend = int(input("Ending Year: "))
                monthstart = int(input("Starting Month(1-12): "))
                monthend = int(input("Ending Month(1-12): "))
                print(db.sortbymonth(monthyearstart, monthyearend, monthstart, monthend))
            elif sortdate == 3:
                dateyearstart = int(input("Starting Year: "))
                dateyearend = int(input("Ending Year: "))
                datemonthstart = int(input("Starting Month(1-12): "))
                datemonthend = int(input("Ending Month(1-12): "))
                datestart = int(input("Starting Date: "))
                dateend = int(input("Ending Date: "))
                print(db.sortbydate(dateyearstart, dateyearend, datemonthstart, datemonthend, datestart, dateend))
        elif sort == 6:
            keyword = input("Enter Keyword: ")
            print(db.keywordsearch(keyword))
            
    elif useri == 3:
        print(db.show_expense())
        delete_expense()
    elif useri == 4:
        print(db.show_expense())
        update_expense()
    elif useri == 5:
        print("1. Show Total Month Spending")
        print("2. Remaining Budget")
        print("3. Set Budget")
        userbudgeti = int(input("Enter choice: "))
        
        if userbudgeti == 1:
            db.totalmonthspend()
        elif userbudgeti == 2:
            db.remainingbudget(budget)
        elif userbudgeti == 3:
            budget = int(input("Enter the Budget you want to set: "))
            db.storebudget(budget)
    elif useri == 6:
        break
    else:
        print("Invalid choice.")