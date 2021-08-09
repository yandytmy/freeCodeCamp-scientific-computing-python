class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        printstring = self.category.center(30, "*") + "\n"
        for item in self.ledger:
            printstring += f"{item['description'][:23]:23}{item['amount']:7.2f}" + "\n"
            # printstring += item["description"][:23] + f"{item['amount']:7.2f}" + "\n"
        balance = self.get_balance()
        printstring += f"Total: {balance:.2f}"
        return printstring

    def deposit(self, amount, description=""):
        temp = {}
        temp["amount"] = amount
        temp["description"] = description
        self.ledger.append(temp)

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            temp = {}
            temp["amount"] = -amount
            temp["description"] = description
            self.ledger.append(temp)
            return True
        return False

    def transfer(self, amount, target_category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + target_category.category)
            target_category.deposit(amount, "Transfer from " + self.category)
            return True
        return False
    
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

def create_spend_chart(categories):
    outputstring = "Percentage spent by category"
    expense = []
    for category in categories:
        temp_expense = 0
        for item in category.ledger:
            temp_expense += -item["amount"] if item['amount'] < 0 else 0
        expense.append(temp_expense)
    total = sum(expense)
    percentage = [i/total * 100 for i in expense]

    for i in range(100, -10, -10):
        outputstring += "\n " + str(i).rjust(3) + "|"
        for j in percentage:
            outputstring += " o " if j > i else "   "
    outputstring += "\n    " + "-" * (3 * len(categories) + 1)
    
    cat_length = []
    for category in categories:
        cat_length.append(len(category.category))
    max_length = max(cat_length)

    for i in range(max_length):
        outputstring += "\n    "
        for j in range(len(categories)):
            outputstring += (" " + categories[j].category[i] + " ") if i < cat_length[j] else "   "
    return outputstring
