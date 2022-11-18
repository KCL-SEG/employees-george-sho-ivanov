"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commission):
        self.name = name
        self.commission = commission

    def get_pay(self):
        if (self.commission):
            return self.get_pay_root() + self.commission.value
        else :
            return self.get_pay_root() 

    def __str__(self):
        if (self.commission):
            return f"{self.name} works on {self.get_description()} and receives {self.commission.description}. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on {self.get_description()}. Their total pay is {self.get_pay()}."

class ContractCommission:
    def __init__(self, contract_num, contract_price):
        self.description = f"a commission for {contract_num} contract(s) at {contract_price}/contract"
        self.value = contract_num * contract_price

class BonusCommission:
    def __init__(self, contract_price):
        self.description = f"a bonus commission of {contract_price}"
        self.value = contract_price

class MonthlyEmployee(Employee):
    def __init__(self, name, salary, commission=None):
        super().__init__(name, commission)
        self.salary = salary

    def get_description(self):
        return f"a monthly salary of {self.salary}"

    def get_pay_root(self):
        return self.salary

class ContractEmployee(Employee):
    def __init__(self, name, contract_hours, contract_rate, commission=None):
        super().__init__(name, commission)
        self.contract_hours = contract_hours
        self.contract_rate = contract_rate

    def get_description(self):
        return f"a contract of {self.contract_hours} hours at {self.contract_rate}/hour"

    def get_pay_root(self):
        return self.contract_hours * self.contract_rate



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie', 4000)
#print(billie)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 100, 25)
#print(charlie)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee', 3000, ContractCommission(4, 200))
#print(renee)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 150, 25, ContractCommission(3, 220))
#print(jan)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie', 2000, BonusCommission(1500))
#print(robbie)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel', 120, 30, BonusCommission(600))
#print(ariel)
