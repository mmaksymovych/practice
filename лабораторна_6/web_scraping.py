"""
Приклад веб-скрейпінгу використовуючи стандартну бібліотеку Python.
Для більш складних завдань рекомендується використовувати:
- requests (замість urllib)
- BeautifulSoup4 або lxml (для парсингу HTML)
"""

import urllib.request
import urllib.error
from html.parser import HTMLParser
import os

# === КЛАС ДЛЯ ПАРСИНГУ HTML ===
class SimpleHTMLParser(HTMLParser):
    """
    Простий HTML-парсер для вилучення даних з HTML-документів.
    Наслідується від HTMLParser зі стандартної бібліотеки Python.
    """
    
    def __init__(self):
        """Ініціалізація парсера"""
        super().__init__()
        self.links = []              # Список для зберігання посилань
        self.in_title = False        # Прапорець: чи знаходимося ми всередині тегу <title>
        self.current_title = ""      # Змінна для зберігання заголовка сторінки
        
    def handle_starttag(self, tag, attrs):
        """
        Метод викликається при знайденні початкового тегу.
        
        Args:
            tag: назва тегу (наприклад, 'a', 'title')
            attrs: список атрибутів тегу у вигляді кортежів (назва, значення)
        """
        if tag == "a":  # Якщо знайдено тег посилання
            for attr, value in attrs:
                if attr == "href":  # Знаходимо атрибут href (адреса посилання)
                    self.links.append(value)  # Додаємо посилання до списку
        if tag == "title":  # Якщо знайдено тег заголовка
            self.in_title = True  # Встановлюємо прапорець
                    
    def handle_data(self, data):
        """
        Метод викликається при знайденні текстового вмісту між тегами.
        
        Args:
            data: текстовий вміст
        """
        if self.in_title:  # Якщо ми всередині тегу <title>
            self.current_title = data.strip()  # Зберігаємо заголовок (видаляємо пробіли)
            
    def handle_endtag(self, tag):
        """
        Метод викликається при знайденні закриваючого тегу.
        
        Args:
            tag: назва закриваючого тегу
        """
        if tag == "title":  # Якщо закривається тег <title>
            self.in_title = False  # Скидаємо прапорець

# === ТЕСТОВІ ДАНІ ===
# Створюємо тестовий HTML файл для демонстрації роботи парсера
sample_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Приклад веб-сторінки для скрейпінгу</title>
</head>
<body>
    <h1>Новини технологій</h1>
    <div class="article">
        <h2><a href="/article1">Python 3.12 випущено з новими функціями</a></h2>
        <p>Опис статті про Python...</p>
    </div>
    <div class="article">
        <h2><a href="/article2">Apple представила новий MacBook</a></h2>
        <p>Опис статті про Apple...</p>
    </div>
    <div class="article">
        <h2><a href="/article3">Веб-скрейпінг: кращі практики</a></h2>
        <p>Опис статті про веб-скрейпінг...</p>
    </div>
</body>
</html>
"""

# === ОСНОВНА ЛОГІКА ПРОГРАМИ ===

# Зберігаємо тестовий HTML у файл
test_file = "sample_page.html"
with open(test_file, "w", encoding="utf-8") as f:
    f.write(sample_html)

# Читаємо та парсимо HTML
try:
    with open(test_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Створюємо екземпляр парсера та обробляємо HTML
    parser = SimpleHTMLParser()
    parser.feed(html_content)  # Передаємо HTML-контент парсеру
    
    # Виводимо результати парсингу
    print(f"Заголовок сторінки: {parser.current_title}")
    print(f"\nЗнайдено посилань: {len(parser.links)}")
    print("\nПосилання на сторінці:")
    for i, link in enumerate(parser.links, 1):
        print(f"{i}. {link}")
    
    # === ПОШУК КЛЮЧОВОГО СЛОВА ===
    keyword = "Python"
    print(f"\n--- Пошук ключового слова '{keyword}' ---")
    if keyword.lower() in html_content.lower():
        print(f"✓ Ключове слово '{keyword}' знайдено на сторінці!")
        # Підрахунок кількості входжень
        count = html_content.lower().count(keyword.lower())
        print(f"Кількість входжень: {count}")
    else:
        print(f"✗ Ключове слово '{keyword}' не знайдено")
    
    # === ПРИКЛАД РОБОТИ З РЕАЛЬНИМ САЙТОМ ===
    print("\n--- Приклад роботи з реальним сайтом (потребує мережі) ---")
    print("Для роботи з реальними сайтами встановіть: pip install requests beautifulsoup4")
    
    # Приклад з urllib (вбудована бібліотека Python)
    try:
        url = "https://www.python.org"
        print(f"Спроба підключення до {url}...")
        # Створюємо запит з заголовками (User-Agent потрібен для деяких сайтів)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        # Відкриваємо URL з таймаутом 5 секунд
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:  # HTTP статус 200 означає успішне підключення
                print(f"✓ Успішне підключення! Код відповіді: {response.status}")
                print(f"Content-Type: {response.headers.get('Content-Type')}")
            else:
                print(f"Код відповіді: {response.status}")
    except urllib.error.URLError as e:
        # Помилка підключення (немає інтернету, неправильний URL тощо)
        print(f"✗ Помилка підключення: {e}")
    except Exception as e:
        # Інші помилки
        print(f"✗ Помилка: {e}")
    
finally:
    # === ОЧИЩЕННЯ ===
    # Видаляємо тестовий файл після завершення роботи
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"\n(Тестовий файл {test_file} видалено)")




