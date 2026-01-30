text = input("Enter text: ")

removed = text.count("a")
text = text.replace("a", "")

print(text)
print(removed)