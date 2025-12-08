"""
Приклади роботи з рядками в Python.
Демонструє основні операції з текстовими даними.
"""

# === ОСНОВНІ ОПЕРАЦІЇ З РЯДКАМИ ===

# --- Конкатенація (об'єднання) рядків ---
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Об'єднуємо два рядки
print(full_name)


# --- Форматування рядків ---
age = 30
# Використовуємо f-string для вставки змінних у рядок
formatted_string = f"My name is {full_name} and I am {age} years old."
print(formatted_string)


# --- Розділення рядка на частини ---
sentence = "Hello,how,are,you?"
words = sentence.split(",")  # Розділяємо рядок за комою
print(words)  # Результат: список ['Hello', 'how', 'are', 'you?']


# --- Об'єднання рядків зі списку ---
words_joined = "-".join(words)  # Об'єднуємо елементи списку через дефіс
print(words_joined)  # Результат: 'Hello-how-are-you?'


# --- Заміна підрядків ---
original_string = "I like apples"
modified_string = original_string.replace("apples", "bananas")  # Замінюємо "apples" на "bananas"
print(modified_string)


# --- Зміна регістру ---
print(original_string.upper())  # Перетворюємо на великі літери
print(original_string.lower())  # Перетворюємо на малі літери


# --- Перевірка наявності підрядка ---
print("apples" in original_string)  # Перевіряємо чи містить рядок слово "apples"


# --- Отримання символу за індексом ---
char_at_index = original_string[2]  # Отримуємо символ на позиції 2 (індексація з 0)
print(char_at_index)  # Результат: 'l' (третій символ)


# --- Ітерація по рядку ---
# Проходимо по кожному символу рядка
for char in original_string:
    print(char, end=" ")  # end=" " дозволяє виводити символи в один рядок через пробіл
