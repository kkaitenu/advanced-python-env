# ===== 1. Класс Person =====
class Person:
    def __init__(self, name, age):
        self._name = name # инкапсуляция (protected)
        self._age = age # инкапсуляция (protected)

    def introduce(self):
        return f"Hi, my name is {self._name} and I am {self._age} years old."


# ===== 2. Класс Student (наследник) =====
class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age) # вызываем конструктор родителя
        self.__grades = grades # инкапсуляция (private)

    # Переопределяем метод introduce() — это полиморфизм
    def introduce(self):
        return f"Hi, I'm {self._name}, a student aged {self._age}."

    # Метод для вычисления среднего балла
    def average_grade(self):
        return sum(self.__grades) / len(self.__grades)

    # Геттер для оценки (пример инкапсуляции)
    def get_grades(self):
        return self.__grades.copy()


# ===== 3. Демонстрация работы =====

# Создаём объект Person
person = Person("Alice", 30)
print(person.introduce())


# Создаём объект Student
student = Student("Bob", 20, [90, 85, 92])
print(student.introduce())
print("Grades:", student.get_grades())
print("Average grade:", student.average_grade())

# Полиморфизм
people = [person, student]
for p in people:
    print(p.introduce())