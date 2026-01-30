text = input()

count = text.count(":")
text = text.replace(":", "%")

print(text)
print(count)