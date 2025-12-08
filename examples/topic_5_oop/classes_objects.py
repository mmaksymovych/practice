"""
Приклади роботи з класами та об'єктами в Python.
Демонструє базові концепції ООП: класи, об'єкти, методи та атрибути.
"""

# === ВИЗНАЧЕННЯ КЛАСУ ===
class Employee:
    """
    Клас Employee представляє співробітника.
    Клас - це шаблон для створення об'єктів.
    """
    
    def __init__(self, emp_id, name, base_salary):
        """
        Конструктор класу - метод, який викликається при створенні об'єкта.
        
        Args:
            emp_id: ідентифікатор співробітника
            name: ім'я співробітника
            base_salary: базова зарплата
        """
        # Атрибути об'єкта (властивості)
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def get_details(self):
        """
        Метод для отримання інформації про співробітника.
        
        Returns:
            рядок з деталями співробітника
        """
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ${self.base_salary:.2f}"
    
    def calculate_salary(self):
        """
        Метод для обчислення зарплати.
        У базовому класі просто повертає базову зарплату.
        
        Returns:
            базова зарплата
        """
        return self.base_salary


# === СТВОРЕННЯ ОБ'ЄКТІВ (ЕКЗЕМПЛЯРІВ) ===
# Об'єкт - це конкретний приклад класу
alice = Employee(101, "Alice", 4000)  # Створюємо об'єкт alice
bob = Employee(102, "Bob", 5000)      # Створюємо об'єкт bob

# Доступ до атрибутів об'єкта
alice.name  # Отримуємо значення атрибута name

# Виклик методів об'єкта
alice.get_details()  # Викликаємо метод get_details() для об'єкта alice
bob.get_details()     # Викликаємо метод get_details() для об'єкта bob

# Виведення результатів
print(alice.get_details())
print(bob.get_details())
