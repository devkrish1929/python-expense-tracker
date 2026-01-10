print("Expense Tracker Started")

amount = input("Enter expense amount: ")
category = input("Enter expense category: ")

with open("expenses.txt", "a") as file:
    file.write(amount + "," + category + "\n")

print("Expense saved successfully!")
