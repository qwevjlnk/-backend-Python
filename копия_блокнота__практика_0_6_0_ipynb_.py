
# **Дисклеймер**

В данной практике будет введен дополнительный критерий: чистота и читаемость кода, а также соблюдение правил описанных в начале практики

---

# Задание 1

**Задача:**

Напишите функцию очищающий список от дубликтов


*Запрещено:*

*   Использовать set() или готовые функции очищающие список от дубликатов

Вввод:

```
apple banana apple 1 3 4 4 5
```


Вывод:

```
apple banana 1 3 4 5
```
"""

def remove_duplicates(input_data):
    uniqe_items = []
    for item in input_data:
        if item not in uniqe_items:
            uniqe_items.append(item)
    return uniqe_items


input_data = ['apple', 'banana', 'apple', '1', '3', '4', '4', '5']
result = remove_duplicates(input_data)
print(result)

"""# Задание 2

**Задача:**

Написать функцию для нахождения простых чисел в диапазоне

Ввод:

```
10, 50
```

Вывод:

```
11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
```
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5) + 1): #проверяем делимость до квадратного корня n
        if n % i == 0:
            return False
    return True


def find_primes(b, e): #begin/end
    primes = []
    for num in range(b, e + 1):
        if is_prime(num):
            primes.append(num)
    return primes


begin = 10
end = 50
result = find_primes(begin, end)
print(result)

"""# Задание 3

Напишите функцию для объединения двух списков (список ключей и список значении) в словарь

*Запрещено:*

*   Использования готовых функции для объединения списков (пример: zip() )

Дано:

```
keys = ['a', 'b', 'c', 'e' ]
values = [1, 2, 3, 4]
```

Вывод:
```
{'a': 1, 'b': 2, 'c': 3, 'e': 4}
```



"""

def list_to_dicts(keys, values):
    dictionary = {}
    for i in range(len(keys)):
        if i < len(values):
            dictionary[keys[i]] = values[i]
        else:
            dictionary[keys[i]] = None
    return dictionary


keys = ['a', 'b', 'c', 'e' ]
values = [1, 2, 3, 4]
result = list_to_dicts(keys, values)
print(result)

"""# Задание 4

Напишите функцию(ии) для подсчета статистических параметров:
*   Сумму
*   Среднее арифметическое
*   Медиану
*   Моду


*Запрещено:*

*   sum()
*   sorted()
*   и других функции предоставляющих готовое решение задания

Дано:

```
numbers = [1, 2, 2, 3, 4, 5, 6, 7, 8 ,9 ,10]

```

Вывод:
```
{'mean': 5.181818181818182, 'median': 5, 'mode': 2, 'sum': 57}
```

"""

def calculate_sum(numbers):  # функция для подсчёта суммы
    total = 0
    for i in numbers:
        total += i
    return total


def calculate_mean(numbers):  # функция для подсчёта ср-его арифм-го
    total_sum = calculate_sum(numbers)
    count = 0
    for i in numbers:
        count += 1
    sr = total_sum / count
    return sr


def puz_sort(adi):  # функция для сортировки (пузырьком)
    n = len(adi)
    sorted_adi = adi[:]
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_adi[j] > sorted_adi[j + 1]:
                sorted_adi[j], sorted_adi[j + 1] == sorted_adi[j + 1], sorted_adi[j]
    return sorted_adi


def calculate_median(numbers):
    sorted_numbers = puz_sort(numbers)
    n = len(sorted_numbers)
    middle = n // 2
    if n % 2 == 0:
        return sorted_numbers[middle - 1] + sorted_numbers[middle] // 2
    else:
        return sorted_numbers[middle]


def calculate_mode(numbers):
    max_count = 0
    mode = None
    for i in range(len(numbers)):
        count = 0
        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                count += 1
        if count > max_count:
            max_count = count
            mode = numbers[i]
    return mode


def calculation_of_statistical_parameters(numbers):
    statistics = {
        'mean': calculate_mean(numbers),
        'meadian': calculate_median(numbers),
        'mode': calculate_mode(numbers),
        'sum': calculate_sum(numbers)
    }
    return statistics


numbers = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(calculation_of_statistical_parameters(numbers))

"""# Задание 5

На ввод поступает строка символов. Строка состоит из слов, которые отделены друг от друга пробелами. Необходимо вывести самое длинное слово и его порядковый номер.

*Запрещено:*

*   len()

Дано:

```
Страдание и боль всегда обязательны для широкого сознания и глубокого сердца.

```

Вывод:
```
Самое длинное слово с номером 5: обязательны
```
"""

def count_characters(word):  # ф-ия для нахожд длины слова
    length = 0
    for char in word:
        length += 1
    return length


def find_longest_word(sentence): # ф-ия для нахожд самого длинного слова
    words = sentence.split()
    max_length = 0
    longest_word = ""
    longest_index = 0

    for i in range(len(words)):
        word_length = count_characters(words[i])
        if word_length > max_length:
            max_length = word_length
            longest_word = words[i]
            longest_index = i + 1
    return longest_word, longest_index


sentence = 'Страдание и боль всегда обязательны для широкого сознания и глубокого сердца.'
longest_word, longest_index = find_longest_word(sentence)
print(f'Самое длинное слово с номером {longest_index} : {longest_word}')

"""# Задание 6

Напишите программу, для управления оценками студентов, со следующими функциями:

* Добавление информации о студенте и его оценках.
* Подсчет среднего балла студента.
* Получение списка всех студентов с их средними баллами.
* Поиск студента по имени и вывод его оценок и среднего балла.




"""

students = {}


def add_student(name, grades):
    if name in students:
        print("Этот студент уже существует.")
    else:
        students[name] = grades
        print("Студент добавлен.")


def calculate_average(name):
    if name in students:
        grades = students[name]
        average = sum(grades) / len(grades)
        return average
    else:
        print("Студент не найден.")
        return None


def list_students():
    for name, grades in students.items():
        average = calculate_average(name)
        print(f"Студент: {name}, Средний балл: {average:.2f}")


def find_student(name):
    if name in students:
        grades = students[name]
        average = calculate_average(name)
        print(f"Оценки студента {name}: {grades}, Средний балл: {average:.2f}")
    else:
        print("Студент не найден.")


add_student("Андрей", [4, 5, 3, 5])
add_student("Иван", [5, 5, 5, 5])
list_students()
find_student("Пётр")

"""# Задание 7


**Задача:**

Создайте приложение-викторину с командной строкой, которое задает пользователям вопросы по различным темам и отслеживает их результаты.

Ключевые особенности:

*   Хранение данных о вопросах и ответах на них, а также баллов за каждый вопрос
*   Реализуйте функцию для представления вопросов, принятия ответов пользователей и предоставления обратной связи о том, являются ли ответы правильными или неправильными.
*  После завершения викторины отобразите общий балл пользователя из числа ответов на вопросы.
*  Реализуйте функцию добавления нового вопроса
*  Реализуйте функцию перемешивания вопросов, для отображения случайного вопроса

"""

import random

questions = []


def add_question(question_text, correct_answer, points):
    question = {
        "question": question_text,
        "answer": correct_answer,
        "points": points
    }
    questions.append(question)


def shuffle_questions():
    random.shuffle(questions)


def quiz():
    score = 0
    shuffle_questions()

    for question in questions:
        print("Вопрос:", question["question"])
        user_answer = input("Ваш ответ: ")
        if user_answer.lower() == question["answer"].lower():
            print("Правильно!")
            score += question["points"]
        else:
            print(f"Неправильно. Правильный ответ: {question['answer']}")
        print()

    print(f"Ваш итоговый счёт: {score} из {sum([q['points'] for q in questions])}")


add_question("Какой язык программирования мы сейчас используем?", "Python", 5)
add_question("Столица Франции?", "Париж", 3)
add_question("Сколько будет 5 + 2?", "7", 2)

quiz()
