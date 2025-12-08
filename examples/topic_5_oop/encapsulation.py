"""
Приклади інкапсуляції в Python.
Інкапсуляція - це приховування внутрішньої реалізації та контроль доступу до даних.
"""

class Employee:
    """
    Клас Employee з інкапсуляцією даних.
    Використовує приватні атрибути та методи доступу (getters/setters).
    """
    
    def __init__(self, emp_id, name, base_salary):
        """
        Конструктор з приватними атрибутами.
        Подвійне підкреслення (__) робить атрибут приватним.
        """
        self.__emp_id = emp_id            # Приватний атрибут (недоступний ззовні)
        self.__name = name                # Приватний атрибут
        self.__base_salary = base_salary  # Приватний атрибут

    # === GETTERS (методи для читання) ===
    @property
    def emp_id(self):
        """Властивість для отримання ID співробітника"""
        return self.__emp_id

    @property
    def name(self):
        """Властивість для отримання імені співробітника"""
        return self.__name

    @property
    def base_salary(self):
        """Властивість для отримання базової зарплати"""
        return self.__base_salary

    # === SETTER (метод для запису з валідацією) ===
    @base_salary.setter
    def base_salary(self, salary):
        """
        Встановлює нову зарплату з перевіркою.
        Якщо зарплата від'ємна, викликає помилку.
        """
        if salary > 0:
            self.__base_salary = salary
        else:
            raise ValueError("Salary must be positive")  # Зарплата повинна бути додатньою
        

    def calculate_salary(self):
        """Обчислює зарплату (базова логіка)"""
        return self.__base_salary

    def get_details(self):
        """Повертає детальну інформацію про співробітника"""
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ${self.base_salary:.2f}"


# === ПРИКЛАД ВИКОРИСТАННЯ ===
emp = Employee(102, "Bob", 4500)
print(emp.get_details())

# Оновлення зарплати через setter
emp.base_salary = 5000  # Використовуємо setter для встановлення нової зарплати
print(emp.get_details())

# Спроба встановити від'ємну зарплату викличе помилку
# emp.base_salary = -1000  # Це викличе ValueError: "Salary must be positive"