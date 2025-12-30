#1
# Функция для нахождения НОД (алгоритм Евклида)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Функция для нахождения НОК
def lcm(a, b):
    return a * b // gcd(a, b)  # // целочисленное деление


# Ввод двух чисел
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# Вычисление НОД и НОК
g = gcd(A, B)
l = lcm(A, B)

# Вывод результатов
print(f"НОД({A}, {B}) = {g}")
print(f"НОК({A}, {B}) = {l}")

#2

import math

# Функция для площади треугольника по формуле Герона
def triangle_area(a, b, c):
    p = (a + b + c) / 2  # полупериметр
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


# Функция для площади четырёхугольника
def quadrilateral_area(a, b, c, d, diagonal):
    # Четырёхугольник делим диагональю на два треугольника
    area1 = triangle_area(a, b, diagonal)
    area2 = triangle_area(c, d, diagonal)
    return area1 + area2


# Ввод данных
a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
d = float(input("Введите сторону d: "))
diag = float(input("Введите диагональ: "))

# Вычисление площади
S = quadrilateral_area(a, b, c, d, diag)

# Вывод результата
print(f"Площадь выпуклого четырёхугольника: {S}")