#=======================================
#       PERSONAL EXPENSE TRACKER
#=======================================

import json
from datetime import date

def add_expense():
    expense=input("What did you spend money on? ")

    if not expense.strip():
        print("Expense cannot be empty.")
        return
    
    try:
        amount=float(input("How much did you spend? ₹"))
    except ValueError:
        print("Please enter a valid number.")
        return
    category=input("What category does your expense come under? ")

    if not category.strip():
            print("Category cannot be empty.")
            return
            
    expenses.append({
        "date": str(date.today()),
        "item": expense,
        "amount": amount,
        "category": category
        })
    
    with open("expenses.json","w") as file:
        json.dump(expenses, file, indent=4)
            
            
    print("\nExpense recorded!")

def view_expense():
    print("\n==== YOUR EXPENSES ====")

    if not expenses:
        print("No expenses recorded yet.")
        return
            
    for expense in expenses:
        print(
            expense.get("date", "Unknown"),
            "-",expense["item"],
            "- ₹", expense["amount"],
            "-", expense["category"]
        )

def view_total():
    total=0
            
    for expense in expenses:
        total=total+expense["amount"]
                
    print("\nTotal spending: ₹",total)

def category_total():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    category_totals={}
    
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
    
        if category in category_totals:
            category_totals[category] = category_totals[category] + amount
        else:
            category_totals[category] = amount
    
    print("\n ====CATEGORY SUMMARY====")
    
    for category in category_totals:
        print(category,": ₹", category_totals[category])

def delete_expense():
    print("==== DELETE EXPENSE ====")

    if not delete_expense:
        print("No expenses added yet for deletion")
        return
    
    for i, expense in enumerate(expenses, start=1):
        print(
            i,
            "=", expense.get("date", "Unknown"),
            "-", expense["item"],
            "- ₹", expense["amount"],
            "-", expense["category"]
        )
    try:
        number= int(input("Enter the expense number to delete: "))
    except ValueError:
        print("please enter a valid expense number")
        return

    if number < 1 or number > len(expenses):
        print("INVALID EXPENSE NUMBER!")
        return
    
    del expenses[number - 1]
    
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
    
    print("Selected Expense Has Been Deleted")

def edit_expense():
    print("==== EDIT EXPENSE ====")

    if not expenses:
        print("No expenses added yet.")
        return
    
    for i, expense in enumerate(expenses, start=1):
        print(
            i,
            "=", expense.get("date", "Unknown"),
            "-", expense["item"],
            "- ₹", expense["amount"],
            "-", expense["category"]
        )

    try:
        number=int(input("Enter the expense number to edit: "))
    except ValueError:
        print("Please enter a valid expense number.")
        return

    if number<1 or number>len(expenses):
        print("Invalid expense number.")
        return
    
    expense = expenses[number - 1]
    
    new_item=input("Enter the new item name: ")

    if not new_item.strip():
        print("Item name cannot be empty.")
        return

    expense["item"]=new_item
    try:
        amount=float(input("Enter a new amount: ₹"))
    except ValueError:
        print("Please enter a Valid number.")
        return

    expense["amount"]=amount
    new_category= input("Enter the new category: ")

    if not new_category.strip():
        print("Please enter a valid category")
        return

    expense["category"]=new_category
    
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
    
    print("Selected Expense Has Been Updated!!")

def monthly_expense():
    if not expenses:
        print("\nNo expenses added yet.")
        return
    
    monthly_totals = {}
    
    for expense in expenses:
        month = expense.get("date", "Unknown")[0:7]
        amount = expense["amount"]
    
        if month in monthly_totals:
            monthly_totals[month] = monthly_totals[month] + amount
        else:
            monthly_totals[month] = amount
    
    print("\n==== MONTHLY SUMMARY ====")
    
    for month in monthly_totals:
        print(month, ": ₹", monthly_totals[month])




print("\n========================================")
print("        PERSONAL EXPENSE TRACKER")
print("========================================")

expenses=[]

try:
    with open("expenses.json","r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

while True:
    print("\n========================================")
    print("              MAIN MENU")
    print("========================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Category Summary")
    print("5. Delete Expense")
    print("6. Edit Expense")
    print("7. Monthly Summary")
    print("8. Exit")
    print("========================================")

    choice= input("\nEnter your choice: ")

    if choice == "1":
        add_expense()
        

    elif choice=="2":
        view_expense()
        

    elif choice=="3":
        view_total()
        

    elif choice=="4":
        category_total()
        

    elif choice == "5":
        delete_expense()
       

    elif choice == "6":
        edit_expense()
        

    elif choice == "7":
        monthly_expense()
        
    elif choice == "8":
        print("\nThank you for using Expense Tracker")
        break

    else:
        print("\nInvalid choice. Please try again.")


