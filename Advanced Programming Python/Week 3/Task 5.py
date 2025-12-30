#1

# Функция для нахождения НОД (алгоритм Евклида)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Функция для вычитания дробей A/B и C/D
def subtract_fractions(A, B, C, D):
    # Вычисляем числитель и знаменатель
    numerator = A * D - B * C
    denominator = B * D

    # Находим НОД для сокращения дроби
    g = gcd(abs(numerator), denominator)  # abs() на случай отрицательного числителя

    # Сокращаем дробь
    numerator //= g
    denominator //= g

    return numerator, denominator


# Ввод данных
A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))

# Вычитание дробей
num, den = subtract_fractions(A, B, C, D)

# Вывод результата
print(f"Результат вычитания: {num}/{den}")

#2

# Функция для вывода всех делителей числа
def print_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(str(i))  # преобразуем в строку для вывода
    print(" ".join(divisors))  # вывод в одной строке через пробел


# Ввод числа
num = int(input("\nВведите число: "))

# Вывод делителей
print("Делители числа:")
print_divisors(num)# Функция для вывода всех делителей числа
def print_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(str(i))  # преобразуем в строку для вывода
    print(" ".join(divisors))  # вывод в одной строке через пробел


# Ввод числа
num = int(input("\nВведите число: "))

# Вывод делителей
print("Делители числа:")
print_divisors(num)