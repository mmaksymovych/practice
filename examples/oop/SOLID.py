# SOLID is an acronym that describes five principles of Object-Oriented design, intended to make software maintainable, scalable, and easy to modify:

# S: Single Responsibility Principle
# O: Open/Closed Principle
# L: Liskov Substitution Principle
# I: Interface Segregation Principle
# D: Dependency Inversion Principle

#🚀 Why SOLID matters?
# Enhances readability and maintainability.
# Makes testing easier.
# Allows for easier updates and extensions.
# Encourages clean, modular design.

# 1. Single Responsibility Principle (SRP)

#BAD
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        pass  # salary calculation logic

    def save_to_db(self):
        pass  # database logic

    def send_notification(self):
        pass  # database logic

john = Employee("John")
john.calculate_salary()
john.save_to_db()

#GOOD
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        pass  # salary logic

class EmployeeDatabaseOperations:
    def save_to_db(self, employee):
        pass  # database logic

class Notifications:
    def sand_notification(self, employee):
        pass  # database logic


john = Employee("John")
salary = john.calculate_salary()

db_operations = EmployeeDatabaseOperations()
db_operations.save_to_db(salary)

notificationsManager = Notifications()
notificationsManager.sand_notification(salary)


# 2. Open/Closed Principle (OCP)
#BAD
class Employee:
    def __init__(self, role):
        self.role = role

    def calculate_salary(self):
        if self.role == 'developer':
            return 4000
        elif self.role == 'designer':
            return 3500
        elif self.role == 'producmanaher':
            return 4500
        elif self.role == 'tesrer':
            return 4500
        
#GOOD
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        return 4000

class Designer(Employee):
    def calculate_salary(self):
        return 3500
    
class ProductManager(Employee):
    def calculate_salary(self):
        return 4500
    

# 3. Liskov Substitution Principle (LSP)
#BAD
class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")
    
#GOOD
class Bird:
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        print("Flying")

class SwimmingBird(Bird):
    def move(self):
        print("Swimming")

class Sparrow(FlyingBird):
    pass

class Penguin(SwimmingBird):
    pass


# 4. Interface Segregation Principle (ISP)
#BAD
class Machine(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass

class Printer(Machine):
    def print(self):
        print("Printing...")

    def scan(self):
        pass  # forced to implement unnecessary method

#GOOD
class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class SimplePrinter(Printer):
    def print(self):
        print("Printing...")

class MultifunctionPrinter(Printer, Scanner):
    def print(self):
        print("Printing...")

    def scan(self):
        print("Scanning...")


# 5. Dependency Inversion Principle (DIP)
#BAD
class MySQLDatabase:
    def save(self, data):
        print(f"Saving {data} to MySQL DB")

class EmployeeManager:
    def __init__(self):
        self.db = MySQLDatabase()  # tightly coupled to MySQLDatabase

    def save_employee(self, data):
        self.db.save(data)

#GOOD
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL DB")

class MongoDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MongoDB")

class EmployeeManager:
    def __init__(self, db: Database):
        self.db = db

    def save_employee(self, data):
        self.db.save(data)

mysql = MySQLDatabase()
mongoDatabase = MongoDatabase()

john = EmployeeManager(mongoDatabase)
smoth = EmployeeManager(mysql)
