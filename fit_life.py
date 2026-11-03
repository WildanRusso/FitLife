# Проект FitLife - MVP версия 1.0
# Функция для ввода целых чисел
def get_int(prompt):
    """Запрашивает положительное целое число."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Ошибка! Введите число больше нуля.")
                continue
            return value
        except ValueError:
            print("Ошибка! Введите целое число, например: 20.")


# Функция для ввода дробных чисел
def get_float(prompt):
    """Запрашивает положительное дробное число."""
    while True:
        try:
            value = float(input(prompt).replace(",", "."))
            if value <= 0:
                print("Ошибка! Введите число больше нуля.")
                continue
            return value
        except ValueError:
            print("Ошибка! Введите число, например: 75 или 1.75.")


# 1. Знакомство
user_name = input("Введите ваше имя: ")
user_age = get_int("Введите ваш возраст: ")

# 2. Сбор данных
user_weight = get_float(
    "Введите ваш вес в килограммах: "
)
user_height = get_float(
    "Введите ваш рост в метрах (например, 1.75): "
)

# 3. Логика расчётов (арифметика)
# Формула ИМТ: вес разделить на рост в квадрате
bmi = user_weight / (user_height ** 2)

# Подсчёт воды: вес * 30 мл
water_needed = user_weight * 0.03

# 4. Вывод результата
print(f"Привет, {user_name}!")
print(f"Ваш возраст: {user_age}")
print(f"Ваш индекс массы тела (ИМТ): {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_needed:.3f} л в день")
print("Расчёт окончен. Будьте здоровы!")

