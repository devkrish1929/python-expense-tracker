from datetime import date

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Validate amount input
        while True:
            amount = input("Enter expense amount: ")
            if amount.isdigit():
                break
            else:
                print("Please enter a number, not words!")

        category = input("Enter expense category: ")

        today = date.today()

        with open("expenses.txt", "a") as file:
            file.write(str(today) + "," + amount + "," + category + "\n")


        print("Expense added successfully!")

    elif choice == "2":
        total = 0
        print("\nExpenses:")

        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue  # skip empty lines
                    try:
                        date_str, amount_str, category = line.split(",", 2)
                        amount_num = int(amount_str)
                        print(f"{date_str} | {category} | {amount_num}")
                        total += amount_num
                    except ValueError:
                        print(f"Skipping invalid entry: {line}")

            print("Total spent:", total)
        except FileNotFoundError:
            print("No expenses found. Add some first!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

