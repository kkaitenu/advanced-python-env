n= float(input())

whole = int(n)               # целая часть
fraction = int((n - whole) * 100)   # дробная часть → целое

result = fraction + (whole / 100)
print(result)