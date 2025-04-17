
class Employee:
    def __init__(self, emp_id, name, years_experience):
        self.emp_id = emp_id
        self.name = name
        self._years_experience = years_experience

    def get_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"
    
    def calculate_salary(self):
        # Basic salary calculation logic
        return self.__salary

class Practician:
    def __init__(self, emp_id, name, years_experience):
        self.emp_id = emp_id
        self.name = name
        self._years_experience = years_experience

    def practice(self): 
        print(f"{self.name} is practicing!")


class JuniorEmployee(Practician, Employee):
    def learn(self):
        print(f"{self.name} is learning new skills!")

    def get_years(self):
            return f"Years: {self._years_experience}"

    
bob = JuniorEmployee(101, "bob", 2)



print(bob.get_years())

