
"""# Задание 1

**Описание:** Создайте иерархию классов для разных типов сотрудников в компании. Реализуйте родительский класс Employee и дочерние классы Manager и Developer. Каждый класс должен иметь метод для расчета зарплаты на основе различных критериев класса.


Отрабатываемый принцип: Наследование
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def __str__(self):
        return f"{self.name} Оклад: {self.salary})"


class Manager(Employee):
    def __init__(self, name, salary, bonus_subordinate):
        super().__init__(name, salary)
        self.bonus_subordinate = bonus_subordinate
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def calculate_salary(self):
        bonus = self.bonus_subordinate * len(self.subordinates)
        return self.salary + bonus

    def __str__(self):
        return f"{self.name} Менеджер, оклад: {self.salary}, кол-во подчиненных: {len(self.subordinates)}"


class Developer(Employee):
    def __init__(self, name, salary, bonus_project):
        super().__init__(name, salary)
        self.bonus_project = bonus_project
        self.completed_projects = 0

    def complete_project(self):
        self.completed_projects += 1

    def calculate_salary(self):
        bonus = self.bonus_project * self.completed_projects
        return self.salary + bonus

    def __str__(self):
        return f"{self.name} Разработчик, оклад: {self.salary}, завершенных п-ов: {self.completed_projects}"



manager = Manager("Егор", 5000, 500)
developer = Developer("Андрей", 4000, 1000)

manager.add_subordinate(developer)

developer.complete_project()

print(manager.calculate_salary())
print(developer.calculate_salary())

print(manager)
print(developer)

"""# Задание 2

**Описание:** Создайте иерархию классов для различных типов транспортных средств (Необходим один родительский класс и 3 дочерних). Реализуйте метод, который позволяет каждому транспортному средству возвращать собственное описание (Метод в каждом классе должен иметь одинаковое название). Продемонстрируйте вызов данного метода для каждого транспортного средства.


Отрабатываемый принцип: Полиморфизм
"""

class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_description(self):
        return f"Это транспортное средство {self.name} с максимальной скоростью {self.speed} км/ч."


class Car(Vehicle):
    def __init__(self, name, speed, num_doors):
        super().__init__(name, speed)
        self.num_doors = num_doors

    def get_description(self):
        return f"Это автомобиль {self.name} с {self.num_doors} дверьми и максимальной скоростью {self.speed} км/ч."


class Bicycle(Vehicle):
    def __init__(self, name, speed, num_gears):
        super().__init__(name, speed)
        self.num_gears = num_gears

    def get_description(self):
        return f"Это велосипед {self.name} с {self.num_gears} передачами и максимальной скоростью {self.speed} км/ч."


class Boat(Vehicle):
    def __init__(self, name, speed, boat_type):
        super().__init__(name, speed)
        self.boat_type = boat_type

    def get_description(self):
        return f"Это лодка {self.name} типа {self.boat_type} с максимальной скоростью {self.speed} км/ч."


car = Car("Камри 3.5", 200, 4)
bicycle = Bicycle("Cube", 30, 21)
boat = Boat("Посейдон", 50, "моторная")

print(car.get_description())
print(bicycle.get_description())
print(boat.get_description())

"""# Задание 3

Онлайн-магазин:
- Создайте модель для онлайн-магазина с классами Product, Order, Customer, и ShoppingCart.
- Product включает информацию о цене, наличии на складе и категории товара.
Order обрабатывает процесс покупки, включая расчет цены с учетом скидок и налогов.
- Customer управляет информацией о пользователе и его истории заказов.
- ShoppingCart позволяет добавлять, удалять и обновлять количество товаров перед оформлением заказа.
"""

class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}): ${self.price}, доступно: {self.stock}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.stock -= quantity
            print(f"Добавлено {quantity} {product.name} в корзину")
        else:
            print(f"Извините, только {product.stock} {product.name} осталось на складе")

    def remove_item(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.stock += item[1]
                print(f"Удалено {item[1]} {product.name} из корзины")
                return
        print(f"{product.name} не найден в корзине")

    def update_quantity(self, product, quantity):
        for index, item in enumerate(self.items):
            if item[0] == product:
                if product.stock + item[1] >= quantity:
                    difference = quantity - item[1]
                    item[0].stock += item[1] - quantity
                    self.items[index] = (item[0], quantity)
                    print(f"Количество {product.name} обновлено до {quantity}")
                    return
                else:
                    print(f"Извините, только {product.stock + item[1]} {product.name} доступно на складе")
        print(f"{product.name} не найден в корзине")

    def get_total_price(self):
        total = 0
        for item in self.items:
            total += item[0].price * item[1]
        return total


class Order:
    def __init__(self, customer, cart):
        self.customer = customer
        self.items = cart.items.copy()
        self.total_price = cart.get_total_price()
        cart.items = []

    def apply_discount(self, discount):
        self.total_price *= (1 - discount)

    def apply_tax(self, tax):
        self.total_price *= (1 + tax)

    def __str__(self):
        order_details = f"Заказ для {self.customer.name}\n"
        for item in self.items:
            order_details += f"{item[0].name}: {item[1]} единиц\n"
        order_details += f"Итого: ${self.total_price:.2f}"
        return order_details


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def place_order(self, cart):
        order = Order(self, cart)  # Создание заказа
        self.orders.append(order)
        print("Заказ оформлен успешно")

    def view_orders(self):
        if not self.orders:
            print("Заказов еще нет")
        else:
            for order in self.orders:
                print(order)
                print("\n-----------------\n")

product1 = Product("Ноутбук", 1000, 5, "Электроника")
product2 = Product("Книга", 20, 10, "Книги")
product3 = Product("Телефон", 500, 15, "Электроника")

customer = Customer("Иван Иванов", "ivan.ivanov@example.com")
cart = ShoppingCart()

cart.add_item(product1, 2)
cart.add_item(product2, 3)
cart.add_item(product3, 1)

print(f"Общая стоимость: ${cart.get_total_price()}")

customer.place_order(cart)
customer.view_orders()

cart.add_item(product2, 2)
customer.place_order(cart)
customer.view_orders()

cart.add_item(product3, 20)  # ошибка
cart.remove_item(product1)   # должно сказать что товара нет в корзине

"""# Задание 4

Симулятор космического корабля:
- Создайте симулятор управления космическим кораблем с классами SpaceShip, CrewMember, и Mission.
- SpaceShip имеет атрибуты для управления топливом, состоянием корпуса, и текущей скоростью.
- CrewMember контролирует здоровье, навыки, и роли в команде (например, пилот, инженер).
- Mission определяет цели, ресурсы, и возможные события (например, аварии, встречи с астероидами).
"""

import random
class SpaceShip:
    def __init__(self, name, fuel, hull_itegrity, speed):
        self.name = name
        self.fuel = fuel
        self.hull_itegrity = hull_itegrity
        self.speed = speed

    def accelerate(self, amount):
        if self.fuel > 0:
            self.speed += amount
            self.fuel -= amount
            print(f"{self.name} ускорился до {self.speed}, топливо: {self.fuel}")
        else:
            print("Недостаточно топлива")

    def take_damage(self, damage):
        self.hull_itegrity -= damage
        print(f"{self.name} получил повреждения, прочность: {self.hull_itegrity}")

    def __str__(self):
        return f"Данные {self.name}: скорость-{self.speed}, целостность-{self.hull_itegrity}, топливо-{self.fuel}"

class CrewMember:
    def __init__(self, name, health, role):
        self.name = name
        self.health = health
        self.role = role

    def perform_task(self, task):
        print(f"{self.name} имеет роль - {self.role}")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил урон, здоровье: {self.health}")

    def __str__(self):
        return f"{self.name}: здоровье-{self.health}, роль-{self.role}"
class Mission:
    def __init__(self, name, objectives, events):
        self.name = name
        self.objectives = objectives
        self.events = events

    def start_mission(self, spaceship, crew):
        print(f"Миссия {self.name} началась!")
        for event in self.events:
            print(f"Событие: {event}")
            if event == "Авария":
                spaceship.take_damage(random.randint(10, 30))
                for member in crew:
                    member.take_damage(random.randint(5, 15))
            elif event == "Встреча с астероидами":
                spaceship.take_damage(random.randint(5, 20))
                spaceship.accelerate(random.randint(5, 10))
                for member in crew:
                    if "Инженер" in member.role:
                        member.perform_task("Ремонт")

    def __str__(self):
        return f"Миссия: {self.name}, Цели: {', '.join(self.objectives)}"

spaceship = SpaceShip("Звездный Крейсер", 100, 100, 0)
crew_member1 = CrewMember("Вова", 100, "Пилот")
crew_member2 = CrewMember("Коля", 100, "Инженер")

mission = Mission("Исследование космоса", ["Найти новые планеты", "Исследовать астероиды"], ["Авария", "Встреча с астероидами", "Ремонт"])

print(spaceship)
print(crew_member1)
print(crew_member2)
print(mission)

spaceship.accelerate(20)
crew_member1.perform_task("Пилотирование")
crew_member2.perform_task("Ремонт")

mission.start_mission(spaceship, [crew_member1, crew_member2])

print(spaceship)
print(crew_member1)
print(crew_member2)

"""# Дополнительно:

**Описание:** создайте консольную версию игры крестики-нолики, используя классы
"""

