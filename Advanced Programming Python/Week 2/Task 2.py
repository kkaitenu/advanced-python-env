a = input().strip()
b = input().strip()

n = len(b)
shifts = set()

# generate all cyclic shifts of b
for i in range(n):
    shifts.add(b[i:] + b[:i])

count = 0

# check substrings of a
for i in range(len(a) - n + 1):
    if a[i:i+n] in shifts:
        count += 1

print(count)