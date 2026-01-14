from expense import Expense

class Category:
    def __init__(self, name):
        self.name = name
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
        else:
            raise IndexError("Invalid expense index")

    def total(self):
        return sum(exp.amount for exp in self.expenses)

    def to_dict(self):
        return {
            "name": self.name,
            "expenses": [e.to_dict() for e in self.expenses]
        }

    @staticmethod
    def from_dict(data):
        category = Category(data["name"])
        for e in data["expenses"]:
            category.add_expense(Expense.from_dict(e))
        return category
