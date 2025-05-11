class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@company.com"

        Employee.num_of_employees += 1

    def getFullName(self):
        return f"{self.first.capitalize() + ' ' + self.last.capitalize()}"
    
    @classmethod
    def update_raise_amt(cls, new_raise_amount):
        cls.raise_amount = new_raise_amount

    #using class method let's create an alternate constructor
    @classmethod
    def from_empstring(cls, empl_str):
        first, last, pay = empl_str.split('-')
        return cls(first, last, pay)
    
    # let's create a static class..a class that does not use any reference to "self" or "cls"
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('sampath','kumar',110000)
emp_2 = Employee('Amit','Sharma',110000)

print(emp_1.getFullName())
print(emp_2.getFullName())
print(f"Total number of emps: {Employee.num_of_employees}")

#get raise amount...again
print(f"Current raise_amount: {emp_1.raise_amount}")
#update employee raise amount
Employee.update_raise_amt(1.25)
#get raise amount...again
print(f"Current raise_amount: {emp_1.raise_amount}")

#create a new employee object using the alternate constructor
#you pass employee details using a string like this sampath-periasamy-70000
new_employee = Employee.from_empstring('Elon-Musk-10')
print(new_employee.getFullName())
print(f"Total number of emps: {Employee.num_of_employees}")

import datetime
my_date = datetime.date(2016,7,8)
print(Employee.is_workday(my_date))