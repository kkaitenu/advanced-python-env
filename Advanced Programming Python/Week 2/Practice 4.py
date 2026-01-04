text = input("Enter text: ")

replacements = text.count("a")
text = text.replace("a", "o")
length = len(text)

print(text)
print(replacements)
print(length)