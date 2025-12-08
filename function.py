"""
Приклади функцій в Python.
Демонструє різні типи функцій: прості операції, пошук у масивах.
"""

# === ПРОСТІ МАТЕМАТИЧНІ ФУНКЦІЇ ===

def sum(a, b):
    """
    Обчислює суму двох чисел.
    
    Args:
        a: перше число
        b: друге число
        
    Returns:
        сума a та b
    """
    return a + b


def returString():
    """
    Повертає привітальний рядок.
    
    Returns:
        рядок "Hello, Guest!"
    """
    return "Hello, Guest!"


def multiply(a, b):
    """
    Обчислює добуток двох чисел.
    
    Args:
        a: перше число
        b: друге число
        
    Returns:
        добуток a та b
    """
    return a * b


def sumAndMultiplyAndSubstractResult(a, b):
    """
    Обчислює складний вираз: (a * b) - (a + b).
    Спочатку обчислює суму та добуток, потім віднімає суму від добутку.
    
    Args:
        a: перше число
        b: друге число
        
    Returns:
        результат обчислення (a * b) - (a + b)
    """
    sumResult = sum(a, b)           # Обчислюємо суму
    multiplyResult = multiply(a, b) # Обчислюємо добуток
    return multiplyResult - sumResult  # Віднімаємо суму від добутку


# === ФУНКЦІЇ ДЛЯ ПОШУКУ В МАСИВАХ ===

def findNumberInArr(arr, target):
    """
    Знаходить індекс першого входження числа у масиві.
    
    Args:
        arr: список чисел для пошуку
        target: число, яке потрібно знайти
        
    Returns:
        індекс знайденого елемента або None, якщо не знайдено
    """
    for i, value in enumerate(arr):
        if value == target:
            return i


def linear_search(arr, target):
    """
    Лінійний пошук елемента у масиві.
    Перевіряє кожен елемент послідовно до знаходження або до кінця масиву.
    
    Args:
        arr: список чисел для пошуку
        target: число, яке потрібно знайти
        
    Returns:
        індекс знайденого елемента або -1, якщо елемент не знайдено
    """
    number = findNumberInArr(arr, target)
    if number:  # Якщо число знайдено (не None)
        return number
    else:   # Якщо число не знайдено
        return -1
