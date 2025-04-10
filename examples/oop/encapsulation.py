class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.__emp_id = emp_id            # Private attribute
        self.__name = name                # Private attribute
        self.__base_salary = base_salary  # Private attribute

    @property
    def emp_id(self):
        return self.__emp_id

    @property
    def name(self):
        return self.__name

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, salary):
        if salary > 0:
            self.__base_salary = salary
        else:
            raise ValueError("Salary must be positive")
        

    def calculate_salary(self):
        # Basic salary calculation logic
        return self.__base_salary

    def get_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ${self.base_salary:.2f}"

emp = Employee(102, "Bob", 4500)
print(emp.get_details())

# Update salary using setter
emp.base_salary = 5000
print(emp.get_details())

# emp.base_salary = -1000  # This would raise a ValueError