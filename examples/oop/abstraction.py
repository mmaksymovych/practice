from abc import ABC, abstractmethod

class Employee(ABC):
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

    @abstractmethod
    def calculate_salary(self, salary):
        pass

    def get_details(self):
        return (f"[{self.__class__.__name__}] ID: {self.emp_id}, Name: {self.name}, "
                f"Salary: ${self.calculate_salary():.2f}")
    

class JuniorEmployee(Employee):

    def calculate_salary(self, salary):
        return salary * 1.25

    def get_details(self):
        return (f"[{self.__class__.__name__}] ID: {self.emp_id}, Name: {self.name}, "
                f"Years of Experience: {self.years_experience}, "
                f"Salary: ${self.calculate_salary():.2f}")
    

john = JuniorEmployee(101, "John", 4000)