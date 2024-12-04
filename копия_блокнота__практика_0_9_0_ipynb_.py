

"""# Дисклеймер

В данной практике вам необходимо применить все ваши знания по темам:

- Функции
- Словари
- Списки
- Множества
- Условные конструкции
- Запросы

и все что было изучено на прошлых практических занятиях

В каждом задании кратко описаны функции, которые необходимо реализовать, детали реализации вы должны продумать самостоятельно

# Задание 0

Создайте функцию по нахождению уникальных элементов из двух списков



```
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
```
"""

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

unique_element = []

for item in a:
    if item not in b:
        unique_element.append(item)

for item in b:
    if item not in a:
        unique_element.append(item)

print(unique_element)

"""# Задание 1

Симулятор виртуального питомца

Цель: создать виртуальный симулятор домашних животных, в котором пользователи смогут заводить питомцев и ухаживать за ними.

Требования:

- Функция для усыновления питомца (имя, тип, возраст).
- Функция для того, чтобы покормить питомца, поиграть с ним или уложить его спать.
- Функция для отображения состояния питомца (голод, радость, энергия).
"""

def pet_adoption():  # функция для создания питомца
    name = input('Введите имя питомца:')
    pet_type = input('Введите тип питомца:')
    age = input('Введите возраст питомца:')
    return {
        "name": name,
        "type": pet_type,
        "age": age,
        "hungry": 50,
        "energy": 50,
        "happines": 50
    }


def feed_pet(pet):  # пер. покормить питомца
    pet["hungry"] += 50
    return f'{pet["name"]} был покормлен. Уровень сытости: {pet["hungry"]}'


def play_with_pet(pet):  # пер. поиграть с питомцем
    pet["energy"] -= 20
    pet["happines"] += 30
    return f'{pet["name"]} поиграл с вами. Уровень энергии: {pet["energy"]}. Уровень радости: {pet["happines"]}.'


def pet_to_bed(pet):  # уложить спать питомца
    pet["energy"] += 30
    pet["hungry"] -= 10
    return f'{pet["name"]} поспал. Уровень энергии: {pet["energy"]}. Уровень сытости: {pet["hungry"]}.'


def get_pet_status(pet):  # статус питомца
    return f'Статус вашего питомца ({pet["name"]}): Сытость - {pet["hungry"]}; Энергия - {pet["energy"]}; Радость - {pet["happines"]}.'


def main():  # основная функция для выбора действий
    pet = pet_adoption()
    while True:
        print("\nВыберите действие:")
        print("1. Покормить питомца")
        print("2. Поиграть с питомцем")
        print("3. Уложить спать питомца")
        print("4. Вывести статус питомца")
        print("5. Выход")

        choice = input()
        if choice == '1':
            result = feed_pet(pet)
        elif choice == '2':
            result = play_with_pet(pet)
        elif choice == '3':
            result = pet_to_bed(pet)
        elif choice == '4':
            result = get_pet_status(pet)
        elif choice == '5':
            print('Вы вышли из игры.')
            break
        else:
            print("Неверный ввод действия.")
            continue

        print(result)


if __name__ == '__main__':
    main()

"""# Задание 2

Рыцарь и дракон

Цель: создать небольшую игру, в которой вам необходимо играть за рыцаря и сразиться с драконом

Требования:

- Создание персонажа (имя, информация о доспехах, оружии, урон, здоровье)
- Управление персонажем и мини сюжет
- Создание дракона (Имя, информация о здоровье и уроне)
- Боевая система (нанесение и получение урона, урон должен быть случайным в заданном диапазоне)
- Реализовать бой между драконом и рыцарем
"""

import random


def create_knight():
    knight = {
        "name": input('Введите имя рыцаря:'),
        "armor": "Стальные доспехи",
        "weapon": "Нефриловый меч",
        "damage": (9, 20),  # диапазон урона
        "health": 100
    }
    return knight


def create_dragon():
    dragon = {
        "name": "Дракон Смауг",
        "damage": (8, 15),  # диапазон урона
        "health": 140
    }
    return dragon


def battle(knight, dragon):
    print(f'{knight["name"]} вступил в битву со Смаугом. Битва начинается!')
    while knight['health'] > 0 and dragon['health'] > 0:
        # Рыцарь атакует дракона
        knight_damage = random.randint(*knight['damage'])
        dragon['health'] -= knight_damage
        print(f'Рыцарь атакует и наносит {knight_damage} урона. '
              f'HP Смауга теперь {dragon["health"]} очков.')

        # Дракон атакует рыцаря
        dragon_damage = random.randint(*dragon['damage'])
        knight['health'] -= dragon_damage
        print(f'Смауг атакует и наносит {dragon_damage} урона. '
              f'HP рыцаря теперь {knight["health"]} очков.')

        if dragon['health'] <= 0:
            print('Дракон Смауг наконец повержен! Теперь гномы снова смогут жить под горой!')
            print(f'Рыцарь {knight["name"]} победил, и Торин Дуббщит поделился с ним сокровищем.')
        elif knight['health'] <= 0:
            print(f'Рыцарь {knight["name"]} пал! Гномы будут мстить Смаугу!')
        elif knight['health'] <= 0 and dragon['health'] <= 0:
          print(f'Рыцарь {knight["name"]} победил дракона, пожертвовав собой!')
          break



def main():
    knight = create_knight()
    dragon = create_dragon()

    print(f'{knight["name"]} одет в {knight["armor"]}.')
    print(f'Оружие рыцаря - {knight["weapon"]}.')
    print(f'Максимальный урон рыцаря с его меча - {knight["damage"][1]}.')
    print(f'Здоровье рыцаря - {knight["health"]}.')
    print(f'Здоровье дракона - {dragon["health"]}, его урон - {dragon["damage"][1]}.')

    while True:
        print('\nВыберите действие:')
        print('1. Сразиться с драконом.')
        print('2. Выйти из игры.')

        choice = input('')
        if choice == '1':
            battle(knight, dragon)
            if knight['health'] <= 0 or dragon['health'] <= 0:
                break
        elif choice == '2':
            print('Вы вышли из игры.')
            break
        else:
            print('Некорректный ввод действия.')


if __name__ == '__main__':
    main()

"""# Задание 3

\Цель - создать менеджера команды Pokémon, который позволит пользователям:

1.   Новый пункт
2.   Новый пункт



- Добавлять покемонов в свою команду. (если такого покемона еще нет в команде)
- Удалять покемонов из их команды.
- Просматривать подробную информацию обо всех покемонах в команде.
- Находить покемона по имени.
- Устраивать тренировочный бой между двумя покемонами

Для данной задачи используйте: https://pokeapi.co/
"""

