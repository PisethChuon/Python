# Base class (Parent)
class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass 1
class Manager(Employee):
    def work(self):
        print(f"{self.name} is preparing reports and assigning tasks.")

# Subclass 2
class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing clean Python code.")

# Subclass 3
class Intern(Employee):
    def work(self):
        print(f"{self.name} is learning and taking notes in meetings.")

# Subclass 4
class Designer(Employee):
    def work(self):
        print(f"{self.name} is designing the new company website.")

# Main program using polymorphism
def start_work_day(employee_list):
    print("Start of the workday...\n")
    for emp in employee_list:
        emp.work()
    print("\nEnd of the workday.")

# Create different employee objects
employees = [
    Manager("Piseth"),
    Developer("Sopheak"),
    Intern("Nita"),
    Designer("Ratanak")
]

# Call the same method on all of them
start_work_day(employees)
