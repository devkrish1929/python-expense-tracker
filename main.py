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
        category_totals = {}

        print("\nExpenses:")

        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    try:
                        date_str, amount_str, category = line.split(",", 2)
                        amount = int(amount_str)

                        print(f"{date_str} | {category} | {amount}")

                        total += amount

                        if category in category_totals:
                            category_totals[category] += amount
                        else:
                            category_totals[category] = amount

                    except ValueError:
                        print(f"Skipping invalid entry: {line}")

            print("\nCategory-wise total:")
            for cat, amt in category_totals.items():
                print(f"{cat} : {amt}")

            print("\nTotal spent:", total)

        except FileNotFoundError:
            print("No expenses found. Add some first!")


    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

