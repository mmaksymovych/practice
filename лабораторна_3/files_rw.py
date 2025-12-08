"""
Приклади роботи з файлами в Python.
Демонструє читання, запис та додавання даних у файли.
"""

import os

# === ФУНКЦІЇ ДЛЯ РОБОТИ З ФАЙЛАМИ ===

# Функція для створення та запису файлу з даними групи
def create_group_file(filename, students):
    """
    Створює новий файл та записує у нього дані про студентів.
    
    Args:
        filename: назва файлу для створення
        students: список кортежів (ім'я, оцінка)
    """
    with open(filename, "w", encoding="utf-8") as file:  # 'w' - режим запису (створює або перезаписує)
        for student, grade in students:
            file.write(f"{student},{grade}\n")  # Записуємо кожного студента у форматі CSV


# Функція для дозапису даних у файл
def append_student_to_file(filename, student, grade):
    """
    Додає нового студента в кінець існуючого файлу.
    
    Args:
        filename: назва файлу
        student: ім'я студента
        grade: оцінка студента
    """
    with open(filename, "a", encoding="utf-8") as file:  # 'a' - режим додавання (append)
        file.write(f"{student},{grade}\n")


# Функція для читання даних з файлу
def read_group_file(filename):
    """
    Читає дані про студентів з файлу.
    
    Args:
        filename: назва файлу для читання
        
    Returns:
        список списків [ім'я, оцінка] для кожного студента
    """
    with open(filename, "r", encoding="utf-8") as file:  # 'r' - режим читання (read)
        lines = file.readlines()  # Читаємо всі рядки файлу
        
        # Повертаємо список, де кожен рядок розділений комою
        return [
            line.strip().split(",") for line in lines  # strip() видаляє зайві пробіли та \n
        ]


# === ПРИКЛАД ВИКОРИСТАННЯ ===

# Створюємо список студентів з оцінками
students_group1 = [("Олег", 85.5), ("Іван", 78.0), ("Марія", 92.0)]

# Створюємо файл та записуємо дані
create_group_file("group1.txt", students_group1)

# Додаємо ще одного студента
append_student_to_file("group1.txt", "Анна", 88.0)

# Читаємо дані з файлу
students = read_group_file("group1.txt")

# Обробляємо дані: додаємо рік до кожної записи
studentsWithYear = []

for student, grade in students:
    studentsWithYear.append((student, grade, 2023))  # Додаємо рік 2023

# Виводимо результат
print(studentsWithYear)





