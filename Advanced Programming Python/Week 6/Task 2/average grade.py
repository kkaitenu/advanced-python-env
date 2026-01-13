import json

# Файлы
input_file = "students.json"
output_file = "students_avg.json"

# Читаем данные из JSON
with open(input_file, "r", encoding="utf-8") as f:
    students = json.load(f)  # Загружаем список словарей

# Добавляем средний балл для каждого студента
for student in students:
    grades = student["grades"]
    average = sum(grades) / len(grades)  # Считаем среднее
    student["average"] = round(average, 2)  # Добавляем новый ключ "average", округляем до 2 знаков

# Сохраняем обновленные данные в новый файл
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4, ensure_ascii=False)  # Красивый вывод с отступами

print(f"Updated data saved to '{output_file}'")