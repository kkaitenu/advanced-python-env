class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner          # private атрибут
        self.__balance = balance      # private атрибут

    # Метод для внесения денег
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    # Метод для снятия денег
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive!")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")

    # Метод для получения текущего баланса
    def get_balance(self):
        return self.__balance

    # Дополнительно можно добавить геттер для владельца
    def get_owner(self):
        return self.__owner

# Создаём счёт
account = BankAccount("Alice", 1000)

# Проверяем баланс
print(f"Owner: {account.get_owner()}, Balance: {account.get_balance()}")

# Делаем депозит
account.deposit(500)       # 500 deposited. New balance: 1500
account.deposit(-100)      # Deposit amount must be positive!

# Пробуем снять деньги
account.withdraw(200)      # 200 withdrawn. New balance: 1300
account.withdraw(2000)     # Insufficient balance!
account.withdraw(-50)      # Withdrawal amount must be positive!

# Финальный баланс
print(f"Final balance: {account.get_balance()}")
