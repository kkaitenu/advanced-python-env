activity = input()
a = int(input())
b = int(input())

match activity:
    case '+':
        print(a + b)
    case '*':
        print(a * b)
    case '/':
        if b == 0:
            print("You can't divide by zero")
    case '-':
        print(a - b)
    case '%':
        print(a % b)
    case _:
        print("Unknown command")