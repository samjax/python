class Employee:
    raise_amount = 1.04
    num_employees_created = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_employees_created += 1
    
    def getFullName(self):
        return f"{self.first.capitalize() + ' ' + self.last.capitalize()} "
    
    @classmethod
    def apply_increment(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_empstring(cls, empstr):
        first, last, pay = empstr.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    

class Developer(Employee):
    pass


# emp1 = Employee('sampath','periasamy',100000)
# print(emp1.getFullName())
# emp2 = Employee.from_empstring('emon-musk-10')
# print(emp2.getFullName())
# import datetime
# print(Employee.is_workday(datetime.date(2025,5,9)))

dev1 = Employee('sampath','periasamy',100000)
print(dev1.getFullName())
print(dev1.email)


# print(help(Employee))
print(help(Developer))