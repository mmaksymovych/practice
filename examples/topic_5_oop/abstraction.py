"""
Приклади абстракції в Python.
Абстракція - це виділення суттєвих характеристик об'єкта та приховування деталей реалізації.
Використовує абстрактні базові класи (ABC) та абстрактні методи.
"""

from abc import ABC, abstractmethod

# === АБСТРАКТНИЙ БАЗОВИЙ КЛАС ===
class Employee(ABC):
    """
    Абстрактний клас Employee.
    Не можна створити об'єкт цього класу напряму.
    Похідні класи повинні реалізувати всі абстрактні методи.
    """
    
    def __init__(self, emp_id, name, base_salary):
        """Конструктор абстрактного класу"""
        self.__emp_id = emp_id        # Приватний атрибут
        self.__name = name            # Приватний атрибут
        self._base_salary = base_salary  # Захищений атрибут

    @property
    def emp_id(self):
        """Властивість для отримання ID"""
        return self.__emp_id

    @property
    def name(self):
        """Властивість для отримання імені"""
        return self.__name

    @abstractmethod
    def calculate_salary(self):
        """
        Абстрактний метод - повинен бути реалізований у похідних класах.
        Кожен тип співробітника має свою логіку обчислення зарплати.
        """
        pass

    def get_details(self):
        """
        Конкретний метод - має реалізацію.
        Використовує абстрактний метод calculate_salary().
        """
        return (f"[{self.__class__.__name__}] ID: {self.emp_id}, Name: {self.name}, "
                f"Salary: ${self.calculate_salary():.2f}")
    

# === КОНКРЕТНА РЕАЛІЗАЦІЯ ===
class JuniorEmployee(Employee):
    """
    Конкретний клас, що наслідується від абстрактного Employee.
    Повинен реалізувати всі абстрактні методи.
    """
    
    def calculate_salary(self):
        """
        Реалізація абстрактного методу.
        Молодші співробітники отримують базову зарплату без бонусів.
        """
        return self._base_salary
    

# === ПРИКЛАД ВИКОРИСТАННЯ ===
john = JuniorEmployee(101, "John", 4000)
print(john.get_details())