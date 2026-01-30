text = input() #Вводим текст

words = text.split()
count = 0

for word in words:
    word = word.strip(".,!?;:()\"'")
    if word.lower().startswith("е"):
        count += 1

print(count)