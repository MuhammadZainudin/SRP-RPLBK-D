class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

class SalaryCalculator:
    def calculate_salary(self, employee):
        return employee.salary

class EmployeeRepository:
    def save_to_database(self, employee):
        print(f"Saving {employee.name} to database...")

class EmployeePrinter:
    def print_employee_details(self, employee):
        print(f"Name: {employee.name}, Position: {employee.position}, Salary: {employee.salary}")

# Penggunaan:
employee = Employee("John Doe", "Developer", 5000)

salary_calculator = SalaryCalculator()
print(f"Salary: {salary_calculator.calculate_salary(employee)}")

employee_repo = EmployeeRepository()
employee_repo.save_to_database(employee)

employee_printer = EmployeePrinter()
employee_printer.print_employee_details(employee)
