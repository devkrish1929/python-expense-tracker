print("Expense Tracker")

amount = input("Enter expense amount: ")
category = input("Enter expense category: ")

with open("expenses.txt", "a") as file:
    file.write(amount + "," + category + "\n")

print("Expense saved successfully!")

print("\nAll Expenses:")

total = 0

with open("expenses.txt", "r") as file:
    for line in file:
        amount, category = line.strip().split(",")
        total += float(amount)
        print(f"Amount: {amount} | Category: {category}")

print("------------------------")
print("Total spent:", total)
