from budget_manager import BudgetManager
from expense import Expense

def menu():
    print("=" * 50)
    print("Personal Budget & Expense Tracker")
    print("=" * 50)
    print("1. Add a new category")
    print("2. Add an expense to a category")
    print("3. View expenses in a category")
    print("4. View total per category")
    print("5. View overall total")
    print("6. Remove an expense")
    print("7. Save data")
    print("8. Load data")
    print("9. List all categories")
    print("0. Exit")
    print("=" * 50)

def main():
    manager = BudgetManager()

    while True:
        menu()
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Category name: ")
                manager.add_category(name)
                print("Category added.")

            elif choice == "2":
                name = input("Category name: ")
                category = manager.get_category(name)
                if not category:
                    print("Category not found.")
                    continue
                desc = input("Description: ")
                amount = float(input("Amount: "))
                category.add_expense(Expense(desc, amount))
                print("Expense added.")

            elif choice == "3":
                name = input("Category name: ")
                category = manager.get_category(name)
                if not category:
                    print("Category not found.")
                    continue
                for i, e in enumerate(category.expenses):
                    print(f"{i}. {e.description} - ${e.amount} ({e.date})")

            elif choice == "4":
                for name, cat in manager.categories.items():
                    print(f"{name}: ${cat.total()}")

            elif choice == "5":
                print(f"Overall Total: ${manager.total_all()}")

            elif choice == "6":
                name = input("Category name: ")
                category = manager.get_category(name)
                if not category:
                    print("Category not found.")
                    continue
                index = int(input("Expense index: "))
                category.remove_expense(index)
                print("Expense removed.")

            elif choice == "7":
                manager.save()
                print("Data saved.")

            elif choice == "8":
                manager.load()
                print("Data loaded.")

            elif choice == "9":
                for name in manager.categories:
                    print(name)

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()

