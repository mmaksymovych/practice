
class Employee:
    def __init__(self, emp_id, name, salary, years_experience):
        self.emp_id = emp_id
        self.name = name
        self._years_experience = years_experience
        self._salary = salary

    def get_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"
    
    def calculate_salary(self):
        # Basic salary calculation logic
        return self._salary



class JuniorEmployee(Employee):
    def learn(self):
        print(f"{self.name} is learning new skills!")

    def get_years(self):
            return f"Years: {self._years_experience}"

    
bob = JuniorEmployee(101, "bob", 1000, 2)



print(bob.get_years())

