a = input().strip()
b = input().strip()

n = len(b)
shifts = set()

# generate all cyclic shifts of b
for i in range(n):
    shifts.add(b[i:] + b[:i]) #берём строку b, отрезаем начало и переносим его в конец.

count = 0

# check substrings of a
for i in range(len(a) - n + 1):
    if a[i:i+n] in shifts: #Берём каждый подряд идущий кусок нужной длины.
        count += 1

print(count)