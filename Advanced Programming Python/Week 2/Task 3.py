s = input().strip()

# extract parts
a = s[0]
op = s[1]
b = s[2]
c = s[4]

# convert known values to integers
def val(ch):
    return int(ch)

if a == 'x':
    b = val(b)
    c = val(c)
    if op == '+':
        x = c - b
    else:  # '-'
        x = c + b

elif b == 'x':
    a = val(a)
    c = val(c)
    if op == '+':
        x = c - a
    else:  # '-'
        x = a - c

else:  # c == 'x'
    a = val(a)
    b = val(b)
    if op == '+':
        x = a + b
    else:  # '-'
        x = a - b

print(x)