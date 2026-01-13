import string
from collections import Counter

# Файл для чтения
input_file = "text.txt"
# Файл для записи анализа
output_file = "analysis.txt"

# Читаем текст и анализируем
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Приводим текст к нижнему регистру
text = text.lower()

# Убираем пунктуацию
translator = str.maketrans("", "", string.punctuation) #убирает лишние символы
text_no_punct = text.translate(translator) #применяет таблицу к тексту, получается строка без пунктуации.

# Разбиваем на строки и слова
lines = text.splitlines() #Разделяет текст на список строк по символам переноса строки \n.
words = text_no_punct.split() #разбивает текст по пробелам на отдельные слова.

# Считаем частоту слов
word_freq = Counter(words)

# Сохраняем результаты в файл
with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"Total lines: {len(lines)}\n")
    f.write(f"Total words: {len(words)}\n\n")
    f.write("Word frequency:\n")
    for word, count in word_freq.most_common():
        f.write(f"{word}: {count}\n")

print("Analysis complete. Check 'analysis.txt'.")