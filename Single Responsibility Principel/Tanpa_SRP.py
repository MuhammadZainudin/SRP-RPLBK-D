class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def save_to_database(self):
        print(f"Saving {self.name} to database...")

    def print_employee_details(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")
