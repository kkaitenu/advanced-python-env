#1

# Функция для нахождения НОД (алгоритм Евклида)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Функция для деления дробей A/B и C/D
def divide_fractions(A, B, C, D):
    # Деление дробей заменяется умножением на обратную дробь
    numerator = A * D
    denominator = B * C

    # Находим НОД числителя и знаменателя
    g = gcd(numerator, denominator)

    # Сокращаем дробь
    numerator //= g
    denominator //= g

    return numerator, denominator


# Ввод данных
A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))

# Деление дробей
num, den = divide_fractions(A, B, C, D)

# Вывод результата
print(f"Результат деления: {num}/{den}")

#2

# Процедура проверки, лежит ли точка внутри круга
def point_inside_circle(x, y, a, b, R):
    # Проверка условия (x - a)² + (y - b)² ≤ R²
    if (x - a) ** 2 + (y - b) ** 2 <= R ** 2:
        return True
    else:
        return False


# Ввод центра круга и радиуса
a = float(input("\nВведите координату a (центр круга): "))
b = float(input("Введите координату b (центр круга): "))
R = float(input("Введите радиус круга: "))

# Список точек
points = [
    (float(input("\nВведите p1: ")), float(input("Введите p2: "))),
    (float(input("\nВведите f1: ")), float(input("Введите f2: "))),
    (float(input("\nВведите l1: ")), float(input("Введите l2: ")))
]

count = 0

# Проверяем каждую точку
for x, y in points:
    if point_inside_circle(x, y, a, b, R):
        count += 1

# Вывод результата
print("\nКоличество точек внутри круга:", count)