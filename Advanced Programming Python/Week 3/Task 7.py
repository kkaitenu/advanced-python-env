#1
# Функция для вычисления площади прямоугольного треугольника
def right_triangle_area(a, b):
    # Площадь = 1/2 * a * b
    return 0.5 * a * b

# Функция для вычисления площади прямоугольника
def rectangle_area(a, b):
    # Площадь = a * b
    return a * b

# Ввод сторон
X = float(input("Введите сторону X: "))
Y = float(input("Введите сторону Y: "))
Z = float(input("Введите сторону Z: "))
T = float(input("Введите сторону T: "))

# Вычисление площади
area_triangle = right_triangle_area(X, Y)
area_rectangle = rectangle_area(Z, T)

# Общая площадь
total_area = area_triangle + area_rectangle

# Вывод результата
print(f"Площадь четырёхугольника: {total_area}")

#2

# Функция для преобразования числа в восьмеричный код длиной 10 символов
def to_octal_10_digits(n):
    # oct(n) возвращает строку вида '0o123', убираем '0o'
    oct_str = oct(n)[2:]
    # Добавляем ведущие нули до длины 10
    return oct_str.zfill(10)

# Ввод числа
num = int(input("\nВведите неотрицательное число: "))

# Вывод восьмеричного кода
print("10-значный восьмеричный код:", to_octal_10_digits(num))