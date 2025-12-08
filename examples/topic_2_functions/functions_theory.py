# === ПРИКЛАДИ РОБОТИ З ФУНКЦІЯМИ В PYTHON ===

# 1. Проста функція (без аргументів, без повернення значення)
def greet():
    """Виводить привітання на екран"""
    print("Hello, world!")

greet()  # Виклик функції. Вивід: Hello, world!


# 2. Функція з позиційними аргументами
def add(x, y):
    """Додає два числа та виводить результат"""
    print(f"The sum of {x} and {y} is {x + y}")

add(4, 6)  # Вивід: The sum of 4 and 6 is 10


# 3. Функція з аргументами за замовчуванням
def greet_user(name="Guest"):
    """Вітає користувача. Якщо ім'я не вказано, використовує 'Guest'"""
    print(f"Hello, {name}!")

greet_user("Bob")  # Вивід: Hello, Bob!
greet_user()       # Вивід: Hello, Guest! (використовує значення за замовчуванням)


# 4. Функція що повертає значення
def multiply(a, b):
    """Множить два числа та повертає результат"""
    return a * b

result = multiply(3, 7)
print(f"Multiplication result: {result}")  # Вивід: Multiplication result: 21


# 5. Функція зі змінною кількістю позиційних аргументів (*args)
def sum_all(*numbers):
    """Обчислює суму будь-якої кількості чисел"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum is: {sum_all(1, 2, 3, 4)}")  # Вивід: Sum is: 10


# 6. Функція зі змінною кількістю іменованих аргументів (**kwargs)
def print_user_info(**info):
    """Виводить інформацію про користувача у вигляді ключ: значення"""
    for key, value in info.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=30, city="New York")
# Вивід:
# name: Alice
# age: 30
# city: New York


# 7. Lambda (анонімна) функція
# Використовується для простих операцій в один рядок
square = lambda x: x ** 2
print(f"Square of 5 is: {square(5)}")  # Вивід: Square of 5 is: 25


# 8. Рекурсивна функція
# Функція, яка викликає сама себе
def countdown(n):
    """Рекурсивний відлік від n до 0"""
    if n == 0:  # Базовий випадок: зупиняємо рекурсію коли n дорівнює 0
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)  # Рекурсивний виклик з n-1

# Приклад використання:
countdown(5)


# 9. Функція для обчислення суми
def sum(a, b):
    """Повертає суму двох чисел"""
    return a + b


# 10. Функція лінійного пошуку
def linear_search(arr, target):
    """
    Шукає елемент у списку та повертає його індекс.
    Якщо елемент не знайдено, повертає -1.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i  # Повертаємо індекс знайденого елемента
    return -1  # Елемент не знайдено

# Приклад використання лінійного пошуку
arr = [1, 3, 5, 7, 9]
target = 5

res = linear_search(arr, target)
print(res)  # Вивід: 2 (індекс елемента 5 у списку)