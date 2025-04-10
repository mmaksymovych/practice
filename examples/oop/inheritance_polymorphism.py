class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.__emp_id = emp_id
        self.__name = name
        self._base_salary = base_salary

    @property
    def emp_id(self):
        return self.__emp_id

    @property
    def name(self):
        return self.__name

    def calculate_salary(self):
        return self._base_salary

    def get_details(self):
        return (f"[{self.__class__.__name__}] ID: {self.emp_id}, Name: {self.name}, "
                f"Salary: ${self.calculate_salary():.2f}")

class JuniorEmployee(Employee):
    def get_details(self):
        return (f"[{self.__class__.__name__}] ID: {self.emp_id}, Name: {self.name}, "
                f"Years of Experience: {self.years_experience}, "
                f"Salary: ${self.calculate_salary():.2f}")


class MiddleEmployee(Employee):
    def __init__(self, emp_id, name, base_salary, years_experience):
        super().__init__(emp_id, name, base_salary)
        self.years_experience = years_experience

    def calculate_salary(self):
        # 10% increment per year of experience
        bonus = self._base_salary * 0.1 * self.years_experience
        return self._base_salary + bonus
    
    def get_details(self):
        return (f"[{self.__class__.__name__}] ID: {self.emp_id}, Name: {self.name}, "
                f"Years of Experience: {self.years_experience}, "
                f"Salary: ${self.calculate_salary():.2f}")
    
    def passExam(self):
        # Example method to simulate passing an exam
        print(f"{self.name} has passed the exam!")
        self.years_experience += 1


john = MiddleEmployee(101, "John", 4000, years_experience=5)




john.get_details()
johnSalary = john.calculate_salary()
print(f"John's salary: ${johnSalary:.2f}")



class SeniorEmployee(Employee):
    def __init__(self, emp_id, name, base_salary, completed_projects):
        super().__init__(emp_id, name, base_salary)
        self.completed_projects = completed_projects

    def calculate_salary(self):
        # Fixed bonus per completed project
        bonus = 500 * self.completed_projects
        return self._base_salary + bonus

# Examples
junior = JuniorEmployee(201, "Carol", 3500)
middle = MiddleEmployee(202, "Dave", 5000, years_experience=3)
senior = SeniorEmployee(203, "Eve", 7000, completed_projects=5)

employees = [junior, middle, senior]

for emp in employees:
    print(emp.get_details())


