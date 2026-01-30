class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # private/protected атрибут (инкапсуляция)

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)  # вызываем конструктор родителя
        self.bonus = bonus

    # Переопределяем метод get_role() → полиморфизм
    def get_role(self):
        return "Manager"

    # Новый метод только для Manager
    def get_bonus(self):
        return self.bonus

def print_employee_info(employees):
    for emp in employees:
        role = emp.get_role()      # вызовет правильный метод, даже если это Manager
        salary = emp.get_salary()
        print(f"{emp.name}: Role = {role}, Salary = {salary}")


# Создаём объекты
e1 = Employee("Alice", 5000)
e2 = Manager("Bob", 8000, 2000)

# Список сотрудников
employees = [e1, e2]

# Выводим информацию
print_employee_info(employees)

# Можно дополнительно показать бонус менеджера
print(f"{e2.name}'s bonus: {e2.get_bonus()}")
