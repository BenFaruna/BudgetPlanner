class BudgetPlanner:
    def __init__(self, **details):
        self.budget = details
    
    def deposit(self, category, amount):
        self.budget[category] = self.budget[category] + amount
        print("Cash deposit successful.")
        print(f"New balance for {category} is: {self.budget[category]}")

    def withdraw(self, category, amount):
        self.budget[category] = self.budget[category] - amount
        print("Take your cash.")
        print(f"New balance for {category} is: {self.budget[category]} ")

    def show(self):
        print("Your budget on items are listed below: \n")
        for category, balance in self.budget.items():
            print(f"{category}: {balance}")
        print("-----------------------------")
    
    def transfer(self, _from, _to, amount):
        self.budget[_from] -= amount
        self.budget[_to] += amount

        print("New budget:")
        print(f"{_from}: {self.budget[_from]}")
        print(f"{_to}: {self.budget[_to]}")
        
            
        


n = BudgetPlanner(food=50000, clothing=5500, entertainment=2000, medicals=10000, savings=200000)
n.show()

n.deposit("food", 10000)
n.withdraw("food", 10000)
n.transfer("savings", "clothing", 10000)
