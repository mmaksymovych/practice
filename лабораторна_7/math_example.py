"""
Приклади побудови графіків математичних функцій у Python.
Для роботи з графіками встановіть: pip install matplotlib numpy
"""

import math

print("=" * 60)
print("ЧАСТИНА 1: Базові математичні операції")
print("=" * 60)

# === БАЗОВІ МАТЕМАТИЧНІ ОПЕРАЦІЇ ===

# Задаємо число для обчислень
x = -5  

# Обчислюємо квадрат числа (x^2)
square = math.pow(x, 2)  # x^2

# Обчислюємо абсолютне значення (модуль) числа
absolute_value = math.fabs(x)

# Виводимо результати
print(f"Square of {x}: {square}")
print(f"Absolute value of {x}: {absolute_value}")

# Додаткові математичні функції з модуля math
print(f"Квадратний корінь з 16: {math.sqrt(16)}")
print(f"sin(π/2): {math.sin(math.pi/2)}")  # Синус кута π/2 (90 градусів)
print(f"cos(0): {math.cos(0)}")            # Косинус кута 0
print(f"e^2: {math.exp(2):.4f}")           # Експонента e в степені 2
print(f"log(10): {math.log(10):.4f}")      # Натуральний логарифм від 10

print("\n" + "=" * 60)
print("ЧАСТИНА 2: Побудова графіків (потребує matplotlib)")
print("=" * 60)

# Спроба побудувати графіки
try:
    import matplotlib.pyplot as plt
    import numpy as np
    
    # === ПІДГОТОВКА ДАНИХ ===
    # Створюємо масив значень x від -10 до 10 з 200 точками
    x_values = np.linspace(-10, 10, 200)
    
    # === СТВОРЕННЯ ФІГУРИ З ПІДГРАФІКАМИ ===
    # Створюємо фігуру з 4 підграфіками (2x2) розміром 12x10 дюймів
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Графіки математичних функцій', fontsize=16, fontweight='bold')
    
    # === ГРАФІК 1: ЛІНІЙНА ТА КВАДРАТИЧНА ФУНКЦІЇ ===
    axes[0, 0].plot(x_values, x_values, label='y = x', color='blue', linewidth=2)
    axes[0, 0].plot(x_values, x_values**2, label='y = x²', color='red', linewidth=2)
    axes[0, 0].set_title('Лінійна та квадратична функції')
    axes[0, 0].set_xlabel('x')
    axes[0, 0].set_ylabel('y')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()
    axes[0, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 0].axvline(x=0, color='k', linewidth=0.5)
    
    # === ГРАФІК 2: ТРИГОНОМЕТРИЧНІ ФУНКЦІЇ ===
    # Створюємо значення x для тригонометричних функцій (від -2π до 2π)
    x_trig = np.linspace(-2*np.pi, 2*np.pi, 200)
    axes[0, 1].plot(x_trig, np.sin(x_trig), label='sin(x)', color='green', linewidth=2)
    axes[0, 1].plot(x_trig, np.cos(x_trig), label='cos(x)', color='orange', linewidth=2)
    axes[0, 1].set_title('Тригонометричні функції')
    axes[0, 1].set_xlabel('x')
    axes[0, 1].set_ylabel('y')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].legend()
    axes[0, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 1].axvline(x=0, color='k', linewidth=0.5)
    
    # === ГРАФІК 3: ЕКСПОНЕНЦІАЛЬНА ТА ЛОГАРИФМІЧНА ФУНКЦІЇ ===
    # Для логарифму x повинен бути > 0, тому починаємо з 0.1
    x_exp = np.linspace(0.1, 5, 200)
    axes[1, 0].plot(x_exp, np.exp(x_exp), label='e^x', color='purple', linewidth=2)
    axes[1, 0].plot(x_exp, np.log(x_exp), label='ln(x)', color='brown', linewidth=2)
    axes[1, 0].set_title('Експоненціальна та логарифмічна функції')
    axes[1, 0].set_xlabel('x')
    axes[1, 0].set_ylabel('y')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()
    axes[1, 0].set_ylim(-5, 20)
    
    # === ГРАФІК 4: ПОЛІНОМІАЛЬНІ ФУНКЦІЇ ===
    axes[1, 1].plot(x_values, x_values**3, label='y = x³', color='darkblue', linewidth=2)
    axes[1, 1].plot(x_values, x_values**2 - 10*x_values + 20, label='y = x² - 10x + 20', color='darkred', linewidth=2)
    axes[1, 1].set_title('Поліноміальні функції')
    axes[1, 1].set_xlabel('x')
    axes[1, 1].set_ylabel('y')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend()
    axes[1, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 1].axvline(x=0, color='k', linewidth=0.5)
    
    # Автоматично налаштовуємо відступи між підграфіками
    plt.tight_layout()
    
    # === ЗБЕРЕЖЕННЯ ГРАФІКІВ ===
    # Зберігаємо графік у файл PNG з роздільною здатністю 100 dpi
    output_file = 'math_graphs.png'
    plt.savefig(output_file, dpi=100, bbox_inches='tight')
    print(f"✓ Графіки успішно створено та збережено у файл '{output_file}'")
    print("  Відкрийте файл для перегляду графіків.")
    
    # Закриваємо фігуру без відображення (щоб не блокувати виконання програми)
    plt.close()
    
    print("\nГрафіки включають:")
    print("  1. Лінійну (y = x) та квадратичну (y = x²) функції")
    print("  2. Тригонометричні функції (sin, cos)")
    print("  3. Експоненціальну (e^x) та логарифмічну (ln(x)) функції")
    print("  4. Поліноміальні функції вищих порядків")
    
except ImportError:
    print("\n⚠ Бібліотеки matplotlib та/або numpy не встановлені.")
    print("  Для побудови графіків виконайте:")
    print("  pip install matplotlib numpy")
    print("\nАльтернативно, можна використовувати онлайн-інструменти:")
    print("  - Desmos (https://www.desmos.com/calculator)")
    print("  - GeoGebra (https://www.geogebra.org/graphing)")

print("\n" + "=" * 60)