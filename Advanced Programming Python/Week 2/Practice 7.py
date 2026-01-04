text = input("Enter text: ")

n = len(text)
half = n // 2

result = ""

for i in range(n):
    if i < half and text[i] == "n":
        result += "*"
    else:
        result += text[i]

print(result)