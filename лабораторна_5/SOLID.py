"""
Принципи SOLID - п'ять принципів об'єктно-орієнтованого дизайну,
призначених для створення підтримуваного, масштабованого та легкого для модифікації програмного забезпечення.

SOLID - це акронім:
S: Single Responsibility Principle (Принцип єдиної відповідальності)
O: Open/Closed Principle (Принцип відкритості/закритості)
L: Liskov Substitution Principle (Принцип підстановки Барбари Лісков)
I: Interface Segregation Principle (Принцип розділення інтерфейсу)
D: Dependency Inversion Principle (Принцип інверсії залежностей)

🚀 Чому важливі принципи SOLID?
- Покращують читабельність та підтримуваність коду
- Роблять тестування простішим
- Дозволяють легше оновлювати та розширювати код
- Сприяють чистому, модульному дизайну
"""

# ============================================================================
# 1. ПРИНЦИП ЄДИНОЇ ВІДПОВІДАЛЬНОСТІ (Single Responsibility Principle - SRP)
# ============================================================================
# Клас повинен мати лише одну причину для зміни.
# Кожен клас повинен відповідати лише за одну функціональність.

# ❌ ПРИКЛАД НЕПРАВИЛЬНОГО ПІДХОДУ
class Employee:
    """Клас, який робить занадто багато речей - порушує SRP"""
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        """Логіка обчислення зарплати"""
        pass

    def save_to_db(self):
        """Логіка роботи з базою даних"""
        pass

    def send_notification(self):
        """Логіка відправки сповіщень"""
        pass

john = Employee("John")
john.calculate_salary()
john.save_to_db()

# ✅ ПРИКЛАД ПРАВИЛЬНОГО ПІДХОДУ
class Employee:
    """Клас відповідає лише за дані співробітника та обчислення зарплати"""
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        """Логіка обчислення зарплати"""
        pass

class EmployeeDatabaseOperations:
    """Окремий клас для роботи з базою даних"""
    def save_to_db(self, employee):
        """Логіка збереження у базу даних"""
        pass

class Notifications:
    """Окремий клас для відправки сповіщень"""
    def send_notification(self, employee):
        """Логіка відправки сповіщень"""
        pass

john = Employee("John")
salary = john.calculate_salary()

db_operations = EmployeeDatabaseOperations()
db_operations.save_to_db(salary)

notificationsManager = Notifications()
notificationsManager.send_notification(salary)


# ============================================================================
# 2. ПРИНЦИП ВІДКРИТОСТІ/ЗАКРИТОСТІ (Open/Closed Principle - OCP)
# ============================================================================
# Класи повинні бути відкриті для розширення, але закриті для модифікації.
# Додаємо нову функціональність через наслідування, а не змінюючи існуючий код.

# ❌ ПРИКЛАД НЕПРАВИЛЬНОГО ПІДХОДУ
class Employee:
    """Клас з великою кількістю if-elif - важко підтримувати"""
    def __init__(self, role):
        self.role = role

    def calculate_salary(self):
        """Додавання нової ролі вимагає зміни цього методу"""
        if self.role == 'developer':
            return 4000
        elif self.role == 'designer':
            return 3500
        elif self.role == 'producmanaher':
            return 4500
        elif self.role == 'tesrer':
            return 4500
        # Щоб додати нову роль, потрібно модифікувати цей метод
        
# ✅ ПРИКЛАД ПРАВИЛЬНОГО ПІДХОДУ
from abc import ABC, abstractmethod

class Employee(ABC):
    """Абстрактний базовий клас - відкритий для розширення"""
    @abstractmethod
    def calculate_salary(self):
        """Кожен похідний клас реалізує свою логіку"""
        pass

class Developer(Employee):
    """Новий клас - розширення без зміни базового класу"""
    def calculate_salary(self):
        return 4000

class Designer(Employee):
    """Новий клас - розширення без зміни базового класу"""
    def calculate_salary(self):
        return 3500
    
class ProductManager(Employee):
    """Новий клас - розширення без зміни базового класу"""
    def calculate_salary(self):
        return 4500
    # Додавання нової ролі не вимагає зміни існуючих класів


# ============================================================================
# 3. ПРИНЦИП ПІДСТАНОВКИ ЛІСКОВ (Liskov Substitution Principle - LSP)
# ============================================================================
# Похідні класи повинні бути замінними на свої базові класи без зміни поведінки програми.

# ❌ ПРИКЛАД НЕПРАВИЛЬНОГО ПІДХОДУ
class Bird:
    """Базовий клас для всіх птахів"""
    def fly(self):
        print("Flying")

class Penguin(Bird):
    """Пінгвін не може літати - порушує LSP"""
    def fly(self):
        raise Exception("Penguins can't fly!")  # Не може замінити Bird
    
# ✅ ПРИКЛАД ПРАВИЛЬНОГО ПІДХОДУ
class Bird:
    """Базовий клас з загальним методом"""
    def move(self):
        """Загальний метод руху"""
        pass

class FlyingBird(Bird):
    """Птах, який літає"""
    def move(self):
        print("Flying")

class SwimmingBird(Bird):
    """Птах, який плаває"""
    def move(self):
        print("Swimming")

class Sparrow(FlyingBird):
    """Горобець - може літати"""
    pass

class Penguin(SwimmingBird):
    """Пінгвін - може плавати, може замінити Bird"""
    pass


# ============================================================================
# 4. ПРИНЦИП РОЗДІЛЕННЯ ІНТЕРФЕЙСУ (Interface Segregation Principle - ISP)
# ============================================================================
# Клієнти не повинні залежати від інтерфейсів, які вони не використовують.
# Краще мати багато специфічних інтерфейсів, ніж один загальний.

# ❌ ПРИКЛАД НЕПРАВИЛЬНОГО ПІДХОДУ
class Machine(ABC):
    """Загальний інтерфейс з усіма можливостями"""
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass

class Printer(Machine):
    """Принтер змушений реалізувати метод scan, який не використовує"""
    def print(self):
        print("Printing...")

    def scan(self):
        pass  # Змушений реалізувати непотрібний метод

# ✅ ПРИКЛАД ПРАВИЛЬНОГО ПІДХОДУ
class Printer(ABC):
    """Окремий інтерфейс для принтера"""
    @abstractmethod
    def print(self):
        pass

class Scanner(ABC):
    """Окремий інтерфейс для сканера"""
    @abstractmethod
    def scan(self):
        pass

class SimplePrinter(Printer):
    """Простий принтер - реалізує лише потрібні методи"""
    def print(self):
        print("Printing...")

class MultifunctionPrinter(Printer, Scanner):
    """Багатофункціональний принтер - реалізує обидва інтерфейси"""
    def print(self):
        print("Printing...")

    def scan(self):
        print("Scanning...")


# ============================================================================
# 5. ПРИНЦИП ІНВЕРСІЇ ЗАЛЕЖНОСТЕЙ (Dependency Inversion Principle - DIP)
# ============================================================================
# Високорівневі модулі не повинні залежати від низькорівневих модулів.
# Обидва повинні залежати від абстракцій.

# ❌ ПРИКЛАД НЕПРАВИЛЬНОГО ПІДХОДУ
class MySQLDatabase:
    """Конкретна реалізація бази даних"""
    def save(self, data):
        print(f"Saving {data} to MySQL DB")

class EmployeeManager:
    """Жорстко прив'язаний до MySQLDatabase"""
    def __init__(self):
        self.db = MySQLDatabase()  # Жорстка залежність від конкретного класу

    def save_employee(self, data):
        self.db.save(data)

# ✅ ПРИКЛАД ПРАВИЛЬНОГО ПІДХОДУ
class Database(ABC):
    """Абстракція для бази даних"""
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    """Конкретна реалізація MySQL"""
    def save(self, data):
        print(f"Saving {data} to MySQL DB")

class MongoDatabase(Database):
    """Конкретна реалізація MongoDB"""
    def save(self, data):
        print(f"Saving {data} to MongoDB")

class EmployeeManager:
    """Залежить від абстракції, а не від конкретної реалізації"""
    def __init__(self, db: Database):
        self.db = db  # Залежність від абстракції

    def save_employee(self, data):
        self.db.save(data)

# Використання - можна легко змінити базу даних
mysql = MySQLDatabase()
mongoDatabase = MongoDatabase()

john = EmployeeManager(mongoDatabase)  # Використовуємо MongoDB
smith = EmployeeManager(mysql)         # Використовуємо MySQL
