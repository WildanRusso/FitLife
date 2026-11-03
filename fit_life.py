# Проект FitLife - MVP версия 1.0

# 1. Знакомство
user_name = input("Введите ваше имя: ")

while True:
    try:
        user_age = int(input("Введите ваш возраст: "))
        if user_age <= 0:
            print("Ошибка! Введите возраст больше нуля.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите целое число, например: 20.")


# 2. Сбор данных
while True:
    try:
        user_weight = float(
            input("Введите ваш вес в килограммах: ").replace(",", ".")
        )
        if user_weight <= 0:
            print("Ошибка! Введите вес больше нуля.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите число, например: 75.")


while True:
    try:
        user_height = float(
            input("Введите ваш рост в метрах: ").replace(",", ".")
        )
        if user_height <= 0:
            print("Ошибка! Введите рост больше нуля.")
            continue
        break
    except ValueError:
        print("Ошибка! Введите число, например: 1.75.")


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
