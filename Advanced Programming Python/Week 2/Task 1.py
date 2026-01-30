s = "".join(input().split())

count = 0

for i in range(len(s) - 4): #двигаемся по строке и берём кусочки длины 5, потому что стрелка состоит из 5 символов
    if s[i:i+5] == ">>-->":
        count += 1
    if s[i:i+5] == "<--<<":
        count += 1

print(count)