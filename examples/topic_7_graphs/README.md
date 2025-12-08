# Тема 7: Побудова графіків математичних функцій у мові Python

## Опис
Цей розділ присвячений візуалізації даних та побудові графіків математичних функцій в Python. Візуалізація є важливим інструментом для аналізу даних, представлення результатів та розуміння математичних концепцій.

## Файли в цьому розділі

### math_example.py
Приклади побудови графіків:
- Лінійні функції
- Квадратичні функції
- Тригонометричні функції
- Експоненціальні та логарифмічні функції
- Багатократні графіки на одній осі
- Налаштування відображення графіків

## Ключові концепції

### Основні бібліотеки

#### Matplotlib
Основна бібліотека для створення графіків:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.show()
```

#### NumPy
Бібліотека для математичних обчислень:
```python
import numpy as np

x = np.linspace(0, 10, 100)  # 100 точок від 0 до 10
y = np.sin(x)
```

#### SciPy
Розширені математичні функції:
```python
from scipy import special
y = special.erf(x)  # Функція помилок
```

### Типи графіків

1. **Лінійні графіки** - `plt.plot()`
   - Функції, залежності
   - Часові ряди

2. **Точкові діаграми** - `plt.scatter()`
   - Кореляції
   - Розподіл даних

3. **Стовпчасті діаграми** - `plt.bar()`
   - Категоріальні дані
   - Порівняння значень

4. **Гістограми** - `plt.hist()`
   - Розподіл частот
   - Статистичний аналіз

5. **Кругові діаграми** - `plt.pie()`
   - Частки та відсотки
   - Композиція даних

6. **Контурні графіки** - `plt.contour()`
   - Функції двох змінних
   - Топографічні карти

### Налаштування графіків

```python
import matplotlib.pyplot as plt
import numpy as np

# Дані
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Створення графіка
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)

# Налаштування
plt.title('Графік синусоїди', fontsize=16)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

# Відображення
plt.show()
```

## Математичні функції

### Тригонометричні
- `np.sin()`, `np.cos()`, `np.tan()`
- `np.arcsin()`, `np.arccos()`, `np.arctan()`

### Експоненціальні та логарифмічні
- `np.exp()` - e^x
- `np.log()` - натуральний логарифм
- `np.log10()` - десятковий логарифм
- `np.power()` - піднесення до степеня

### Поліноми
- `np.poly1d()` - створення поліному
- `np.polyfit()` - апроксимація поліномом

### Статистичні
- `np.mean()`, `np.median()`, `np.std()`
- Генератори випадкових чисел

## Розширені можливості

### Підграфіки (Subplots)
```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, y1)
ax2.plot(x, y2)
```

### 3D графіки
```python
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
```

### Анімація
```python
from matplotlib.animation import FuncAnimation
ani = FuncAnimation(fig, update_function, frames=100)
```

### Стилізація
```python
plt.style.use('seaborn')  # Використання готового стилю
```

## Необхідні бібліотеки
```bash
pip install matplotlib
pip install numpy
pip install scipy  # опціонально
```

## Альтернативні бібліотеки
- **Seaborn** - статистична візуалізація
- **Plotly** - інтерактивні графіки
- **Bokeh** - веб-візуалізація
- **Altair** - декларативна візуалізація
- **Pandas plotting** - інтеграція з DataFrame

## Як використовувати
```bash
python math_example.py
```

## Типові застосування
- Візуалізація математичних функцій
- Представлення експериментальних даних
- Науковий аналіз
- Фінансові графіки
- Статистичні звіти
- Навчальні матеріали

