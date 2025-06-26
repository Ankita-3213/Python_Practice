import datetime

expenses = []
categories = ("Food", "Travel", "Utilities", "Entertainment", "Other")

def add_expense():
    date = input("Enter date(yyyy-mm-dd): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expenses.append([date,amount,category])
    print("Expense added. ")

def monthly_summary():
    month = input("Enter month: ")
    year = input("Enter year: ")
    total = 0

    for exp in expenses:
        date_p = exp[0].split("-")
        exp_year = date_p[0]
        exp_month = date_p[1]
        if exp_month == month and exp_year == year:
            total = total + exp[1]
    print("Your monthly total is:",total)

while True:
    print("\n1. Add Expense")
    print("2. Show monthly expenses")
    print("3. Exit")
    option = input("Enter your option: ")
    
    
    if option == "1":
        add_expense()
    elif option == "2":
        monthly_summary()
    elif option == "3":
        print("Thanks for visit")
        break
    else:
        print("Enter option 1 or 2")