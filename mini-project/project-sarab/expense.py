from datetime import datetime

class Expense:
    def __init__(self, description, amount, date=None):
        self.description = description
        self.amount = amount
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value <= 0:
            raise ValueError("Amount must be positive")
        self._amount = value

    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            data["description"],
            data["amount"],
            data["date"]
        )
