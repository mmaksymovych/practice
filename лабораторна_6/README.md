# Тема 6: Збір даних з веб-документів за допомогою мови Python

## Опис
Цей розділ присвячений веб-скрейпінгу - процесу автоматичного збору та обробки даних з веб-сайтів. Python пропонує потужні інструменти для парсингу HTML, роботи з HTTP-запитами та обробки веб-даних.

## Файли в цьому розділі

### web_scraping.py
Приклади роботи з веб-даними:
- Відправка HTTP-запитів
- Парсинг HTML-документів
- Пошук та вилучення даних
- Робота з веб-формами
- Обробка помилок при роботі з мережею
- Збереження зібраних даних

## Ключові концепції

### Основні бібліотеки

#### requests
Бібліотека для відправки HTTP-запитів:
```python
import requests
response = requests.get('https://example.com')
```

#### BeautifulSoup
Бібліотека для парсингу HTML та XML:
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
```

#### lxml
Швидкий парсер HTML/XML:
```python
from lxml import html
tree = html.fromstring(page_content)
```

#### Selenium
Для роботи з динамічними веб-сайтами (JavaScript):
```python
from selenium import webdriver
driver = webdriver.Chrome()
```

### Основні завдання веб-скрейпінгу

1. **Отримання HTML-коду**
   - GET запити
   - POST запити
   - Обробка cookies та сесій

2. **Парсинг HTML**
   - Пошук елементів за тегами
   - Пошук за CSS-селекторами
   - Пошук за XPath
   - Робота з атрибутами

3. **Вилучення даних**
   - Текстовий контент
   - Зображення та файли
   - Таблиці
   - Посилання

4. **Обробка даних**
   - Очищення тексту
   - Форматування
   - Валідація
   - Збереження у файли/БД

## Етика веб-скрейпінгу

### ⚠️ Важливі правила:
- Перевіряйте `robots.txt` сайту
- Додавайте затримки між запитами
- Не перевантажуйте сервери
- Поважайте авторські права
- Дотримуйтесь Terms of Service
- Не збирайте персональні дані без дозволу

### Кращі практики
```python
# Додавання затримки
import time
time.sleep(1)  # Пауза 1 секунда

# Вказування User-Agent
headers = {'User-Agent': 'Mozilla/5.0 ...'}
requests.get(url, headers=headers)

# Обробка помилок
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Помилка: {e}")
```

## Типові задачі
- Збір цін з інтернет-магазинів
- Моніторинг новин
- Збір контактної інформації
- Аналіз конкурентів
- Дослідження ринку
- Збір наукових даних

## Необхідні бібліотеки
```bash
pip install requests
pip install beautifulsoup4
pip install lxml
pip install selenium  # для динамічних сайтів
```

## Як використовувати
```bash
python web_scraping.py
```

## Альтернативні інструменти
- **Scrapy** - фреймворк для масштабного скрейпінгу
- **Playwright** - сучасна альтернатива Selenium
- **httpx** - асинхронна альтернатива requests
- **parsel** - для роботи з XPath та CSS селекторами

