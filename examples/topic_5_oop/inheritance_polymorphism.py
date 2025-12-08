"""
Приклади наслідування та поліморфізму в Python.
Поліморфізм - це можливість об'єктів різних класів реагувати на однакові виклики по-різному.
"""

# === БАЗОВИЙ КЛАС ===
class Employee:
    """
    Базовий клас для всіх співробітників.
    Визначає загальну структуру та поведінку.
    """
    
    def __init__(self, emp_id, name, base_salary):
        """Ініціалізація базових атрибутів співробітника"""
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

    def calculate_salary(self):
        """Базовий метод обчислення зарплати"""
        return self._base_salary

    def get_details(self):
        """Повертає детальну інформацію про співробітника"""
        return (f"[{self.__class__.__name__}] ID: {self.emp_id}, Name: {self.name}, "
                f"Salary: ${self.calculate_salary():.2f}")


# === ПОХІДНІ КЛАСИ ===
class JuniorEmployee(Employee):
    """
    Клас для молодших співробітників.
    Використовує стандартний метод get_details() з батьківського класу.
    """
    pass  # Не додає нових методів, використовує базову реалізацію


class MiddleEmployee(Employee):
    """
    Клас для середніх співробітників.
    Демонструє перевизначення методів (поліморфізм).
    """
    
    def __init__(self, emp_id, name, base_salary, years_experience):
        """
        Конструктор з додатковим параметром - роками досвіду.
        super() викликає конструктор батьківського класу.
        """
        super().__init__(emp_id, name, base_salary)
        self.years_experience = years_experience

    def calculate_salary(self):
        """
        Перевизначений метод обчислення зарплати.
        Додає бонус 10% за кожен рік досвіду.
        """
        bonus = self._base_salary * 0.1 * self.years_experience
        return self._base_salary + bonus
    
    def get_details(self):
        """Перевизначений метод з додатковою інформацією про досвід"""
        return (f"[{self.__class__.__name__}] ID: {self.emp_id}, Name: {self.name}, "
                f"Years of Experience: {self.years_experience}, "
                f"Salary: ${self.calculate_salary():.2f}")
    
    def passExam(self):
        """
        Додатковий метод, специфічний для середніх співробітників.
        Симулює проходження іспиту та збільшення досвіду.
        """
        print(f"{self.name} has passed the exam!")
        self.years_experience += 1


# === ПРИКЛАД ВИКОРИСТАННЯ ===
john = MiddleEmployee(101, "John", 4000, years_experience=5)

# Виклик методів об'єкта
john.get_details()
johnSalary = john.calculate_salary()
print(f"John's salary: ${johnSalary:.2f}")


class SeniorEmployee(Employee):
    """
    Клас для старших співробітників.
    Має свою логіку обчислення зарплати на основі завершених проектів.
    """
    
    def __init__(self, emp_id, name, base_salary, completed_projects):
        """Конструктор з параметром кількості завершених проектів"""
        super().__init__(emp_id, name, base_salary)
        self.completed_projects = completed_projects

    def calculate_salary(self):
        """
        Перевизначений метод обчислення зарплати.
        Додає фіксований бонус 500 за кожен завершений проект.
        """
        bonus = 500 * self.completed_projects
        return self._base_salary + bonus


# === ДЕМОНСТРАЦІЯ ПОЛІМОРФІЗМУ ===
# Створюємо об'єкти різних класів
junior = JuniorEmployee(201, "Carol", 3500)
middle = MiddleEmployee(202, "Dave", 5000, years_experience=3)
senior = SeniorEmployee(203, "Eve", 7000, completed_projects=5)

# Зберігаємо їх у списку (поліморфізм)
employees = [junior, middle, senior]

# Викликаємо один і той же метод для різних об'єктів
# Кожен об'єкт виконує метод по-своєму (поліморфізм)
for emp in employees:
    print(emp.get_details())


