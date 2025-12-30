#1
def square_area(a):
    return a * a


def rectangle_area(a, b):
    return a * b


def circle_area(r):
    return 3.14 * r * r

print("1 - Square")
print("2 - Rectangle")
print("3 - Circle")

choice = int(input("Choose shape: "))

if choice == 1:
    a = float(input("Enter side: "))
    print("Area =", square_area(a))

elif choice == 2:
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    print("Area =", rectangle_area(a, b))

elif choice == 3:
    r = float(input("Enter radius: "))
    print("Area =", circle_area(r))

def array_sum_and_avg(arr):
    total = sum(arr)
    average = total / len(arr)
    return total, average

#2
for i in range(1, 4):
    print(f"\nArray {i}")

    n = int(input("Enter size (<=15): "))
    arr = []

    for j in range(n):
        arr.append(int(input()))

    s, avg = array_sum_and_avg(arr)

    print("Sum =", s)
    print("Average =", avg)