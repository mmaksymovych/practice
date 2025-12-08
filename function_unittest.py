"""
Модуль для тестування функцій з function.py.
Використовує фреймворк unittest для автоматичного тестування.
"""

import function
import unittest   # Фреймворк для тестування

class BaseMathOperations(unittest.TestCase):
    """
    Клас тестів для базових математичних операцій.
    Наслідується від unittest.TestCase для використання методів тестування.
    """
    
    def test_sum(self):
        """Тест функції додавання"""
        result = function.sum(3, 3)   # Викликаємо функцію sum з аргументами 3 та 3
        # Перевіряємо, що результат дорівнює 6
        self.assertEqual(result, 6)

    def test_multiply(self):
        """Тест функції множення"""
        result = function.multiply(3, 3)   # Викликаємо функцію multiply з аргументами 3 та 3
        # Перевіряємо, що результат дорівнює 9
        self.assertEqual(result, 9)

    def test_sumAndMultiplyAndSubstractResult(self):
        """Тест складної функції: (a * b) - (a + b)"""
        result = function.sumAndMultiplyAndSubstractResult(3, 3)
        # Для a=3, b=3: (3*3) - (3+3) = 9 - 6 = 3
        self.assertEqual(result, 3)

    def test_linear_search_success(self):
        """Тест лінійного пошуку - успішний випадок (елемент знайдено)"""
        arr = [1, 3, 5, 7, 9, 11, 15]
        target = 7
        expected_index = 3  # Очікуваний індекс елемента 7 у масиві

        result = function.linear_search(arr, target)

        # Перевіряємо, що знайдено правильний індекс
        self.assertEqual(result, expected_index)

    def test_linear_search_failed(self):
        """Тест лінійного пошуку - невдалий випадок (елемент не знайдено)"""
        arr = [1, 3, 5, 7, 9, 11, 15]
        target = 20  # Елемент, якого немає в масиві
        expected_index = -1  # Очікуваний результат, коли елемент не знайдено

        result = function.linear_search(arr, target)

        # Перевіряємо, що повернуто -1 (елемент не знайдено)
        self.assertEqual(result, expected_index)


if __name__ == '__main__':
    # Запускаємо всі тести, якщо файл виконується напряму
    unittest.main()
