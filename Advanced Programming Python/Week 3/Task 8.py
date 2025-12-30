#1
# Функция для проверки, делится ли число на все свои цифры
def divisible_by_own_digits(num):
    for digit in str(num):
        d = int(digit)
        if d == 0 or num % d != 0:
            return False
    return True


# Ввод числа n
n = int(input("Введите n: "))

# Список подходящих чисел
result = []

for i in range(1, n + 1):
    if divisible_by_own_digits(i):
        result.append(i)

# Вывод результата
print("Числа, делящиеся на все свои цифры:", result)

#2
# Процедура для замены первого и последнего элемента массива
def swap_first_last(arr):
    if len(arr) > 1:  # проверка, что массив больше 1 элемента
        arr[0], arr[-1] = arr[-1], arr[0]


# Ввод длины массива
m = int(input("\nВведите длину массива: "))

# Ввод элементов массива
A = []
print("Введите элементы массива:")
for i in range(m):
    A.append(int(input()))

# Вывод оригинального массива
print("Оригинальный массив:", A)

# Замена первого и последнего элемента
swap_first_last(A)

# Вывод результирующего массива
print("Массив после замены первого и последнего элемента:", A)