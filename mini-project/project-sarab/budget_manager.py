import json
from category import Category

class BudgetManager:
    def __init__(self):
        self.categories = {}

    def add_category(self, name):
        if name in self.categories:
            raise ValueError("Category already exists")
        self.categories[name] = Category(name)

    def get_category(self, name):
        return self.categories.get(name)

    def total_all(self):
        return sum(cat.total() for cat in self.categories.values())

    def save(self, filename="budget_data.json"):
        with open(filename, "w") as f:
            json.dump(
                {name: cat.to_dict() for name, cat in self.categories.items()},
                f,
                indent=4
            )

    def load(self, filename="budget_data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.categories = {
                    name: Category.from_dict(cat)
                    for name, cat in data.items()
                }
        except FileNotFoundError:
            pass
