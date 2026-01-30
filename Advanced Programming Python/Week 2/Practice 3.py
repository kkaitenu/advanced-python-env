text = input("Enter text: ")

removed = text.count(".")
text = text.replace(".", "")

print(text)
print(removed)