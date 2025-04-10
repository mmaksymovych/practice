import os

# Функція для створення та запису файлу з даними групи
def create_group_file(filename, students):
    with open(filename, "w") as file:
        for student, grade in students:
            file.write(f"{student},{grade}\n")

# Функція для дозапису даних у файл
def append_student_to_file(filename, student, grade):
    with open(filename, "a") as file:
        file.write(f"{student},{grade}\n")

# Функція для читання даних з файлу
def read_group_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

        return [
            line.strip().split(",") for line in lines
            ]


# Приклад використання
#students_group1 = [("Олег", 85.5), ("Іван", 78.0), ("Марія", 92.0)]
#create_group_file("group1.txt", students_group1)
#append_student_to_file("group1.txt", "Анна", 88.0)

students = read_group_file("group1.txt")

studentsWithYear = []

for student, grade in students:
    studentsWithYear.append((student, grade, 2023))

print(studentsWithYear)





