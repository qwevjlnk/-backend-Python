
# Задание (совместное с преподавателем)

Напишите систему для учёта отпусков с возможностью узнавать, сколько дней отпуска осталось у того или иного сотрудника.
Для этого создайте класс Employee со следующими методами:

- Метод consume_vacation должен отвечать за списание дней отпуска.

Единственный параметр этого метода (кроме self) — количество потраченных отпускных дней (целое число).

При вызове метода consume_vacation соответствующее количество дней должно вычитаться из общего числа доступных отпускных дней сотрудника.

Чтобы определить число доступных отпускных дней конкретного сотрудника, в классе опишите атрибут экземпляра remaining_vacation_days, который по умолчанию будет равен значению атрибута класса vacation_days, и используйте этот атрибут в работе метода.

- Метод get_vacation_details должен возвращать остаток отпускных дней сотрудника в формате: ```Остаток отпускных дней: <число>.```


Чтобы проверить работу программы:
1. Создайте экземпляр класса Employee.
2. Вызовите метод consume_vacation, указав подходящее значение аргумента, например 7.
3. Вызовите метод get_vacation_details.
"""



"""# Задание 1

Задание:

Создайте класс с именем Rectangle который имеет:
- Атрибуты ширины и высоты.
- Метод расчета площади.
- Метод расчета периметра.
- Метод отображения размеров прямоугольника.

Создайте экземпляр класса Rectangleи продемонстрируйте его функциональность.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def rectangle_size(self):
        print(f'Width of rectangle: {self.width}; Height of rectangle: {self.height}')


rectangle = Rectangle(5, 10)
rectangle.rectangle_size()
area = rectangle.calculate_area()
per = rectangle.calculate_perimeter()
print(area)
print(per)

"""# Задание 2

Задание: Создайте мини версию банковской системы:


Инструкции:


1. Создайте класс BankAccountсо следующими атрибутами:
    - account_holder -  владелец счета
    - balance - баланс счета

2. Реализуйте следующие методы:
    - Метод для инициализации владельца счета: имя владельца счета и установите начальный баланс на 0.
    - deposit(amount): Добавьте указанную сумму к балансу.
    - withdraw(amount): Вычесть указанную сумму из баланса, если средств достаточно; в противном случае вывести предупреждение.
    - get_balance(): Возврат текущего баланса.


Создайте объект класса и продемонстрируйте его возможности
"""

class BankAccountсо:

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Недостаточно средств')

    def get_balance(self):
        return self.balance


account = BankAccountсо("Ivan Ivanov")
balance = account.deposit(1000)
account.withdraw(111)
account.get_balance()
print(f'current balance:{account.get_balance()}')

"""# Задание 3

Возьмите код и задание (Рыцарь и дракон) из предыдущей практики и реализуйте его с применением классов
"""

import random


class Knight:
    def __init__(self, name):
        self.name = name
        self.armor = "Steel armor"
        self.weapon = "Jade Sword"
        self.damage = (9, 20)
        self.health = 100

    def attack(self):
        return random.randint(*self.damage)

    def take_damage(self, damage):
        self.health -= damage


class Dragon:
    def __init__(self):
        self.name = "Dragon Smaug"
        self.damage = (8, 15)
        self.health = 140

    def attack(self):
        return random.randint(*self.damage)

    def take_damage(self, damage):
        self.health -= damage


def battle(knight, dragon):
    print(f'{knight.name} entered into battle with {dragon.name}. The battle begins')
    while knight.health > 0 and dragon.health > 0:
        knight_damage = knight.attack()
        dragon.take_damage(knight_damage)
        print(f'The knight attacks and deals {knight_damage} damage')
        print(f'HP of {dragon.name}: {dragon.health}')

        if dragon.health <= 0:
            print(f'{dragon.name} is dead')
            break

        dragon_damage = dragon.attack()
        knight.take_damage(dragon_damage)
        print(f'{dragon.name} attacks and deals {dragon_damage} damage')
        print(f'HP of {knight.name}: {knight.health}')

        if knight.health <= 0:
            print(f'{knight.name} is dead')
            break

    if knight.health <= 0 and dragon.health <= 0:
        print('The knight and dragon died in battle')


def main():
    knight_name = input('Enter name: ')
    knight = Knight(knight_name)
    dragon = Dragon()

    print(f'{knight.name} dressed in {knight.armor}')
    print(f'{knight.name} wields a {knight.weapon}')
    print(f'Current HP {knight.name}: {knight.health}')
    print(f'Maximum damage of the knight: {knight.damage[1]}')
    print(f'{dragon.name}\'s current HP: {dragon.health}')
    print(f'Maximum damage of {dragon.name}: {dragon.damage[1]}')

    while True:
        print('\nSelect action')
        print('1. Fight the dragon')
        print('2. Escape from battle')

        choice = input('')
        if choice == '1':
            battle(knight, dragon)
            # Reset dragon health for a new battle
            dragon = Dragon()
        elif choice == '2':
            print('You’re a coward!')
            break
        else:
            print('Incorrect input')


if __name__ == '__main__':
    main()

"""# Дополнительное задание

Задача: Система управления библиотекой

**Цель**
Создайте простую систему управления библиотекой, которая позволит пользователям добавлять книги, брать книги, возвращать книги и просматривать список доступных книг.

**Требования**

1. **Определение класса**:
   – Создайте класс с именем «Book» со следующими атрибутами:
     - `title`
     - `автор`
     - `isbn`
     - `is_borrowed` (по умолчанию `False`)

2. **Класс библиотеки**:
   - Создайте класс с именем Library, который управляет коллекцией книг.
   - Класс должен иметь следующие методы:
     - `__init__(self)`: инициализирует пустой список книг.
     - `add_book(self, book: Book)`: добавляет новую книгу в библиотеку.
     - `borrow_book(self, isbn: str)`: помечает книгу как заимствованную. Если книга не найдена или уже взята, выведите соответствующее сообщение.
     - `return_book(self, isbn: str)`: помечает книгу как возвращенную. Если книга не найдена или не была взята взаймы, выведите соответствующее сообщение.
     - `list_available_books(self)`: печатает список всех доступных книг в библиотеке.
     - `find_book(self, isbn: str)`: возвращает объект книги, если он найден, в противном случае возвращает `None`.

3. **Взаимодействие с пользователем**:
   - Создайте простое текстовое меню, которое позволит пользователям:
     - Добавить книгу
     - Одолжить книгу
     - Вернуть книгу
     - Список доступных книг
     - Выйти из программы
"""

