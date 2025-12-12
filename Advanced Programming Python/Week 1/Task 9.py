ticket = input()

# первые три цифры
sum1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
# последние три
sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

print("YES" if sum1 == sum2 else "NO")