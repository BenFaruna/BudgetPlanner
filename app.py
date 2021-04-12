class BudgetPlanner:
    def __init__(self, **details):
        keys = list()
        value = list(details.values())

        for key in details.keys():
            keys.append(key.lower())

        self.budget = dict(zip(keys, value))
    
    def deposit(self, category, amount):
        category  = category.lower()

        try:
            self.budget[category] = self.budget[category] + amount
            print("Cash deposit successful.")
            print(f"New balance for {category} is: {self.budget[category]}")
        except KeyError:
            print(f"No budget for {category}.")
            print("Creating new category...")

            self.budget.update({category : amount})
            print("Category added.")
            print("You can transfer balance to the right category if wrong.\n")

    def withdraw(self, category, amount):
        category = category.lower()

        try:
            if self.budget[category] > amount:
                self.budget[category] = self.budget[category] - amount
                print("Take your cash.")
                print(f"New balance for {category} is: {self.budget[category]} ")
            else:
                print("Insufficient funds, deposit and try again later.")

        except KeyError:
            print("Category does not exist, check spelling and try again.")
        

    def show(self):
        print("Your budget on items are listed below: \n")
        for category, balance in self.budget.items():
            print(f"{category}: {balance}")
        print("-----------------------------")
    
    def transfer(self, _from, _to, amount):
        try:
            _from = _from.lower()
            _to = _to.lower()
            self.budget[_from] -= amount
            self.budget[_to] += amount

            print("New budget:")
            print(f"{_from}: {self.budget[_from]}")
            print(f"{_to}: {self.budget[_to]}")
            print("----------------------------")
        except Exception:
            print("Cannot transfer funds, check to see if category is correct or if you have enough funds to transfer.")


n = BudgetPlanner(Food=50000, clothing=5500, entertainment=2000, medicals=10000, savings=200000)

n.show()
# n.deposit("food", 10000)
# n.withdraw("Food", 10000)
# n.transfer("savings", "clothing", 10000)
