
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def get_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"
    
    def calculate_salary(self):
        # Basic salary calculation logic
        return self.__salary

class JuniorEmployee(Employee):
    def __init__(self, emp_id, name, years_experience):
        super().__init__(emp_id, name)
        self.years_experience = years_experience

    

class MiddleEmployee(Employee):
    def __init__(self, emp_id, name, years_experience):
        super().__init__(emp_id, name)
        self.years_experience = years_experience


john = MiddleEmployee(101, "John", 5)
print(john.get_details())