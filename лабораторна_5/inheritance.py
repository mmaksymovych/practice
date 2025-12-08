"""
Приклади наслідування в Python.
Наслідування - це механізм створення нового класу на основі існуючого.
"""

# === БАЗОВИЙ КЛАС (БАТЬКІВСЬКИЙ) ===
class Employee:
    """
    Базовий клас Employee.
    Містить загальні властивості та методи для всіх співробітників.
    """
    
    def __init__(self, emp_id, name, salary, years_experience):
        """
        Конструктор базового класу.
        
        Args:
            emp_id: ідентифікатор співробітника
            name: ім'я співробітника
            salary: зарплата
            years_experience: роки досвіду
        """
        self.emp_id = emp_id
        self.name = name
        self._years_experience = years_experience  # Захищений атрибут (одне підкреслення)
        self._salary = salary                      # Захищений атрибут

    def get_details(self):
        """Повертає базову інформацію про співробітника"""
        return f"Employee ID: {self.emp_id}, Name: {self.name}"
    
    def calculate_salary(self):
        """
        Обчислює зарплату з урахуванням бонусу за досвід.
        Бонус: 10% від зарплати за кожен рік досвіду.
        """
        bonus = self._salary * 0.1 * self._years_experience
        self._salary = self._salary + bonus

    def get_salary(self):
        """Повертає поточну зарплату"""
        return self._salary


# === ПОХІДНИЙ КЛАС (ДОЧІРНІЙ) ===
class JuniorEmployee(Employee):
    """
    Клас JuniorEmployee наслідується від Employee.
    Успадковує всі методи та атрибути батьківського класу
    та може додавати свої власні методи.
    """
    
    def learn(self):
        """Метод, специфічний для молодших співробітників"""
        print(f"{self.name} is learning new skills!")

    def get_years(self):
        """Повертає кількість років досвіду"""
        return f"Years: {self._years_experience}"


# === ПРИКЛАД ВИКОРИСТАННЯ ===
# Створюємо об'єкт похідного класу
bob = JuniorEmployee(101, "bob", 1000, 2)

# Викликаємо метод з батьківського класу
bob.calculate_salary()  # Обчислює зарплату з бонусом

# Викликаємо метод з дочірнього класу
print(bob.get_years())  # Виводить роки досвіду

