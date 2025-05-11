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
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def update_increment(cls, amount):
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
    raise_amount = 1.50

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def del_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp_list(self):
        for emp in self.employees:
            print("-->", emp.first)

# emp1 = Employee('sampath','periasamy',100000)
# print(emp1.getFullName())
# emp2 = Employee.from_empstring('emon-musk-10')
# print(emp2.getFullName())
# import datetime
# print(Employee.is_workday(datetime.date(2025,5,9)))

dev1 = Developer('sampath','periasamy',1000, 'java')
dev2 = Developer('amit','sharma',2000, 'python')

manager = Manager('Becky', 'Huber', 3000, [])
# print(manager.email)

# manager.add_emp(dev1)
# manager.add_emp(dev2)
# manager.print_emp_list()

# manager.del_emp(dev1)
# print(manager.email)
# manager.print_emp_list()

print(f"Is dev1 a instance of Employee : {isinstance(dev1, Employee)}")
print(f"Is Developer a subclass of Employee : {issubclass(Developer, Employee)}")
print(f"Is Manager a subclass of Developer : {issubclass(Manager, Developer)}")