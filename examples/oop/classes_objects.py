class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def get_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ${self.base_salary:.2f}"
    
    def calculate_salary(self):
        # Basic salary calculation logic
        return self.base_salary

# Creating an object (instance)
alice = Employee(101, "Alice", 4000)
bob = Employee(102, "Bob", 5000)

alice.name
alice.get_details()
bob.get_details()





print(alice.get_details())
print(bob.get_details())

