class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

        Employee.num_of_employees += 1

    def getFullName(self):
        return self.first.capitalize() + " " + self.last.capitalize()

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('sampath', 'kumar', 1000)
emp_2 = Employee('corey', 'shafer', 2000)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email) 
# print(emp_1.getFullName())
# print(emp_2.getFullName())
#Callign using class name
# print(Employee.getFullName(emp_1))
# emp_1.raise_amount = 1.10
# emp_2.raise_amount = 1.20
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)

# print(emp_1.__dict__)
# print(Employee.__dict__)
# print(emp_2.__dict__)

print(f"Total num of employees: {Employee.num_of_employees}")