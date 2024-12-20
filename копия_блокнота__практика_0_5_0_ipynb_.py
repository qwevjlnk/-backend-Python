
"""# **Задание 1**

Дан словарь, содержащий имена и возраст людей, напишите программу выводящую возраст человека по имени

Дано:

```
{"Alice": 25, "Bob": 30, "Charlie": 35}
```

Вввод:


```
Alice
```

Вывод:


```
Alice 25
```
"""

peoples = {"Alice": 25, "Bob": 30, "Charlie": 35}
name = input('')
print(f'{name}', {peoples[name]})

"""# **Задание 2**

Дан список, состоящий из целых чисел, необходимо написать функцию считающую сумму всех положительных четных чисел списка

Ввод:

```
1, 2, 3, 4, 5, 6, 7, 8, 9
```

Вывод:


```
20
```

***Запрещено:***

*   Использование готовых функций для суммирования чисел
"""

def sum_chet_pos(numbers):
    tot_sum = 0
    for num in numbers:
        if num > 0 and num % 2 == 0:
            tot_sum += num
    return tot_sum

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_chet_pos(n))

"""# **Задание 3**

Дан словарь, содержащий название фрукта и его цвет, выведите список всех желтых фруктов


Дано:

```
fruits_and_colors = {
    "apple": "red",
    "banana": "yellow",
    "mango": "yellow",
    "orange": "orange",
    "lemon": "yellow",
    "grape": "purple"
}
```

Вывод:


```
Yellow fruits:
banana
lemon
mango
```
"""

fruits = {
    "apple": "red",
    "banana": "yellow",
    "mango": "yellow",
    "orange": "orange",
    "lemon": "yellow",
    "grape": "purple"
}

yellow_fruits = []

for fruit, collor in fruits.items():
    if collor == "yellow":
        yellow_fruits.append(fruit)

print(yellow_fruits)

"""# **Задание 4**

Дан словарь, необходимо написать функцию меняющую ключ и значение местами

Дано:


```
{"a": 1, "b": 2, "c": 3}
```

Вывод:

```
{1: 'a', 2: 'b', 3: 'c'}
```
"""

def swap_numbers(dict):
    swap_dict = {}
    for key in dict:
        value = dict[key]
        swap_dict[value] = key
    return swap_dict

d = {"a": 1, "b": 2, "c": 3}
print(swap_numbers(d))

"""```
# Выбран кодовый формат
```

# **Задание 5**

Дан список слов, неограниченной длинны, сформируйте словарь, где в качестве ключа будет слово, а в качестве значения количество символов

**Критерии**


*   Словарь необходимо отсортировать по убыванию количества элементов в списке.
*   Подсчет элементов должен быть реализован в отдельной функции
*   Сортировка пары `ключ:значение` должна быть реализована также в виде отдельной функции




Дано:
```
['apple','banana','orange','apple','apple','banana']
```


Вывод:
```
{'apple':3, 'banana': 2, 'orange': 1}
```

***Запрещено:***

*   Использование готовых функций для сортировки словаря
*   Использование готовых функций для подсчета элементов
"""

def count_word(word_list):#функция для подсчёта слов и преобразования их в словарь
    count_dict = {} #
    for word in word_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict

def sort_dict(count_d): # функция для сортировки словаря по значенияем (по убыванию)
    sorted_dict = {}
    while count_d:
        max_key = None
        max_V = -1
        for key, value in count_d.items():
            if value > max_V:
                max_V = value
                max_key = key
        sorted_dict[max_key] = max_V
        del count_d[max_key]
    return sorted_dict


words = ['apple','banana','orange','apple','apple','banana']
count_w = count_word(words)
sor = sort_dict(count_w)
print(sor)

"""# **Задание 6**

Дан словарь, содержащий информацию о людях, необходимо:



*   Вывести всех людей старше 30 лет
*   Вывести список городов и количество людей из словаря проживающих в них
*   Вывести список профессий и список людей для каждой профессии

**Критерии**

Каждый из пунктов необходимо реализовать в виде функции
"""

people_info = {
    "Alice": {"age": 25, "city": "New York", "occupation": "Engineer"},
    "Bob": {"age": 30, "city": "Los Angeles", "occupation": "Designer"},
    "Charlie": {"age": 35, "city": "Chicago", "occupation": "Teacher"},
    "Diana": {"age": 28, "city": "Miami", "occupation": "Doctor"},
    "Ethan": {"age": 40, "city": "Seattle", "occupation": "Chef"},
    "Frank": {"age": 32, "city": "Atlanta", "occupation": "Lawyer"},
    "Gabriella": {"age": 29, "city": "San Francisco", "occupation": "Software Engineer"},
    "Harrison": {"age": 38, "city": "Denver", "occupation": "Architect"},
    "Isabella": {"age": 26, "city": "Washington D.C.", "occupation": "Journalist"},
    "Julian": {"age": 42, "city": "Miami", "occupation": "Musician"},
    "Kate": {"age": 31, "city": "Philadelphia", "occupation": "Nurse"},
    "Lucas": {"age": 36, "city": "Nashville", "occupation": "Businessman"},
    "Mia": {"age": 27, "city": "Atlanta", "occupation": "Artist"},
    "Natalie": {"age": 39, "city": "Portland", "occupation": "Writer"},
    "Oliver": {"age": 44, "city": "Minneapolis", "occupation": "Professor"},
    "Penelope": {"age": 33, "city": "San Diego", "occupation": "Marketing Manager"},
    "Quincy": {"age": 41, "city": "Nashville", "occupation": "Singer"},
    "Rachel": {"age": 34, "city": "Cleveland", "occupation": "Teacher"},
    "Sophia": {"age": 29, "city": "Nashville", "occupation": "Engineer"},
    "Tessa": {"age": 37, "city": "Miami", "occupation": "Lawyer"}
}
def get_over_30(people): #>30years
    return {name: info for name, info in people.items() if info['age'] > 30}

def get_cities_count(people): #citysd
    city_count = {}
    for info in people.values():
        city = info['city']
        if city in city_count:
            city_count[city] +=1
        else:
            city_count[city] = 1
    return city_count

def get_occupation(people):
    occupation_dict = {}
    for name, info in people.items():
        occupation = info['occupation']
        if occupation in occupation_dict:
            occupation_dict[occupation].append(name)
        else:
            occupation_dict[occupation] = [name]
    return occupation_dict

a = get_over_30(people_info)
b = get_cities_count(people_info)
c = get_occupation(people_info)
print(a)
print(b)
print(c)



"""# **Задание 7**

Задание: Разработка системы отзывов о предметах

Описание: Создать программу на Python для хранения и управления отзывами о предметах учебного курса. Программа должна позволять пользователям добавлять, просматривать и удалять отзывы, а также вычислять средний балл по заданному предмету.

**Функционал:**

*   Добавление отзыва и оценки:
   *   Пользователь может ввести название предмета, оценку (от 1 до 5) и текст отзыва.
   *   Отзывы должны храниться в структуре данных (например, словаре), где ключом будет название предмета, а значением - список отзывов (каждый отзыв может хранить оценку и комментарий).
*   Просмотр отзывов и оценок:
   *   Пользователь может запросить отзывы для указанного предмета.
   *   Если для указанного предмета есть отзывы, программа должна отобразить список всех отзывов и соответствующих оценок.
*   Удаление отзыва:
   *   Пользователь может удалить отзыв по индексу. Необходимо заранее уведомить пользователя о том, какие отзывы доступны для удаления.
   *   Программа должна обработать ситуацию, когда индекс введен неправильно.
*   Вычисление среднего балла по предмету:
   *   Пользователь может ввести название предмета, и программа должна вычислить и вывести средний балл по всем отзывам для этого предмета.
   *   Если отзывов нет, программа должна сообщить об этом.


**Критерии:**

*   Код должен быть оформлен в виде функций
*   Необходимо обрабатывать неправильный ввод пользователя
*   Должны быть комментарии к функциям
*   Присутсвует весь дополнительный функционал



**Опционально:**

Предлагаю вам добавить свои критерии оценки или вопросы, на которые должен ответить студент, чтобы оценить пару
"""

reviews = {}  #словарь с отзывами


def add_review(course, rating, comment):
    """
    добавление отзыва для курса
    """
    if course in reviews:
        reviews[course].append([rating, comment])
    else:
        reviews[course] = [[rating, comment]]
    print("Отзыв добавлен!")


def view_reviews(course):
    """
    посмотреть озыв
    """
    if course in reviews:
        print("Отзывы для", course, ":")
        for i in range(len(reviews[course])):
            print(i + 1, "Оценка:", reviews[course][i][0], "Комментарий:", reviews[course][i][1])
    else:
        print("Нет отзывов для этого курса")


def delete_review(course, index):
    """
    удаляет отзыв через индекс
    """
    try:
        if course in reviews:
            reviews[course].pop(index - 1)
            print("Отзыв удален")
        else:
            print("Нет отзывов для этого курса")
    except:
        print("Неверный индекс")


def calculate_average_rating(course):
    """
     считает средний балл
    """
    total = 0
    count = 0
    if course in reviews:
        for review in reviews[course]:
            total += review[0]
            count += 1
        if count > 0:
            print("Средний балл для", course, ":", total / count)
        else:
            print("Нет отзывов для этого курса")
    else:
        print("Нет отзывов для этого курса")


def main():
    """
  менюшка
    """
    while True:
        print("\n1. Добавить отзыв")
        print("2. Посмотреть отзывы")
        print("3. Удалить отзыв")
        print("4. Рассчитать средний балл")
        print("5. Выйти")

        option = input("Выберите действие: ")

        if option == '1':
            course = input("Введите название курса: ")
            rating = input("Введите оценку (от 1 до 5): ")
            comment = input("Введите комментарий: ")
            try:
                rating = int(rating)
                if rating < 1 or rating > 5:
                    print("Оценка должна быть от 1 до 5")
                else:
                    add_review(course, rating, comment)
            except:
                print("Ошибка! Оценка должна быть числом")

        elif option == '2':
            course = input("Введите название курса: ")
            view_reviews(course)

        elif option == '3':
            course = input("Введите название курса: ")
            index = input("Введите номер отзыва для удаления: ")
            try:
                index = int(index)
                delete_review(course, index)
            except:
                print("Ошибка! Индекс должен быть числом")

        elif option == '4':
            course = input("Введите название курса: ")
            calculate_average_rating(course)

        elif option == '5':
            print("Программа завершена")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()

"""> Комментарий от преподавателя:

> В последнем задании данное условие определено неверно

```
rating = int(rating)
if rating < 1 or rating > 5:
    print("Оценка должна быть от 1 до 5")
else:
    add_review(course, rating, comment)
```



"""

