# Проект FitLife - MVP версия 1.0

# 1. Знакомство
user_name = input("Введите ваше имя: ")
user_age = int(input("Введите ваш возраст: "))

# 2. Сбор данных
user_weight = float(input("Введите ваш вес в килограммах: "))
user_height = float(input("Введите ваш рост в метрах: "))

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
print("Расчет окончен. Будьте здоровы!")
