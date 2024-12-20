

"""***Дисклеймер***

В даннёой практике запрещено использования функций:


*   sum()
*   min()
*   max()
*   average()
*   reversed()
*   sorted()
*   готовые функции или библиотеки

**Задача 1:**



Интернет-магазин предлагает следующие условия скидок:

*   Для заказов больше 1000 единиц, клиент получает скидку 5%. Если клиент использует промокод SUPERDISCOUNT, он получает скидку 10%.
*  Для заказов стоимостью более 5000 единиц, клиент получает скидку 15%, а использование промокода SUPERDISCOUNT увеличивает скидку до 20%.

Этап 1:
Ввод:
```
Введите стоимость единицы товара: 5
Введите количество товара: 1000
Введите промокод: GiVEMEDISCONT
```

Вывод:

```
Ваша скидка: 5%
Итоговая сумма: 4750.0
```
Этап 2:

Оформите ваш код в виде функции
"""

def calculate(price, count, promo=''):
    tot_cost = price * count

    if tot_cost > 1000:
        discont = 0.05
    elif tot_cost > 5000:
        discont = 0.15
    else:
        discont = 0.0

    if 'SUPERDISCOUNT' in promo:
        if tot_cost <= 1000:
            pass
    elif tot_cost <= 5000:
        discont += 0.05
    elif tot_cost > 1000:
        discont += 0.05

    return tot_cost * (1- discont), f'{discont * 100}'

tot_cost, mes = calculate(5, 5001)
print('Ваша скидка:', mes)
print('Итоговая сумма', tot_cost)

"""**Задача 2:**

Этап 1:
Напишите программу способную отфильтровать список и вывести только положительные элементы


Ввод:
```
-1 5 1 2 -3
```

Вывод:

```
5 1 2
```

Этап 2:

Оформите ваш код в виде функции
"""

def filter_numbers(numbers):
    return [num for num in numbers if num > 0]

my_nums = [-1, 213, 22, -4, 5, 6, -22]
res = filter_numbers(my_nums)
print(res)

"""**Задача 3:**

Этап 1:
Напишите программу реализующую Алгоритм Евклида


> Алгоритм Евклида – это алгоритм нахождения наибольшего общего делителя (НОД) пары целых чисел.



Ввод:
```
30 18
```

Вывод:

```
6
```

Этап 2:
Оформите ваш код в виде функции

"""

def nod(a, b):
    while b != 0:
        a, b  = b, a % b
    return a

num1 = 120
num2 = 3200
res = nod(num1, num2)
print(res)

"""**Задача 4:**

Этап 1:
Напишите функцию программу, которая принимает строку и возвращает список слов и количество их упомнинаний в предложении

Этап 2:
Оформите ваш код в виде функции

Ввод:
```
apple banana apple
```

Вывод:

```
apple: 2,
banana: 1
```
"""

def count_words(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

sent = 'apple banana apple'
res = count_words(sent)
print(res)

"""**Задача 5:**

Этап 1:
Детектор анаграмм Напишите программу на Python, которая принимает в качестве входных данных две строки и проверяет, являются ли они анаграммами друг друга

Этап 2:
Оформите ваш код в виде функции

Ввод:
```
listen, silent
```

Вывод:

```
True
```
"""

def anagr(word1, word2):
    let1 = list(word1)
    let2 = list(word2)
    let1.sort()
    let2.sort()
    return let1 == let2

n1 = 'listen'
n2 = 'silent'
if anagr(n1, n2) == True:
    print('yes')
else:
    print('no')

"""**Задача 5:**

Шифр ​​Цезаря

Напишите программу на Python, которая реализует шифр Цезаря, простой метод шифрования, который заменяет каждую букву буквой на фиксированное количество позиций вниз по алфавиту. Программа должна запрашивать у пользователя сообщение и значение сдвига, а затем шифровать и расшифровывать сообщение.

Этап 1:

Напишите код для реализации данной задачи

Этап 2:

Оформите код в виде нескольких функций:

* Зашифровывает сообщение
* Расшифровывает сообщение
"""

def encypt(message, key):
    enc_msg = ""
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for ch in message.lower():
        if ch in alpha:
            idx = alpha.find(ch)
            new_idx = (idx + key) % len(alpha)
            enc_ch = alpha[new_idx]
            enc_msg += enc_ch
        else:
            enc_msg += ch

    return enc_msg

def decrypt(enc_msg, key):
    dec_msg = ""
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for ch in enc_msg:
        if ch in alpha:
            idx = alpha.find(ch)
            new_idx = (idx - key) % len(alpha)
            dec_ch = alpha[new_idx]
            dec_msg += dec_ch
        else:
            dec_msg += ch

    return dec_msg

def main():
    msg = input("Введите текст, который хотите зашифровать: ")
    k = int(input("Введите ключ: "))  # 1-25

    enc_msg = encypt(msg, k)
    print(f"Твой шифр готов: {enc_msg}")

if __name__ == "__main__":
    main()

"""**Задача 6**

Задача: «Банковская система»

Создайте программу Python, которая имитирует базовую банковскую систему. Система должна иметь следующие функции:

Требования
*   Система должна позволять клиентам создавать счета и хранить их балансы.
*   Система должна позволять клиентам вносить и снимать деньги со своих счетов.
*   Система должна позволять клиентам проверять свой текущий баланс.
*   Система должна позволять клиентам переводить деньги между счетами.
*   Система должна отслеживать транзакции (депозиты, снятия и переводы) и иметь возможность печатать детали транзакций.


Задачи
1. Реализуйте банковскую систему, используя только базовые конструкции Python, такие как def, lists, if, elif и else, без классов или словарей.
Определите функции для создания счетов, внесения и снятия денег, получения балансов счетов, перевода денег между счетами, а также создания и печати транзакций.
2. Напишите основную функцию, которая демонстрирует использование банковской системы путем создания счетов, внесения и снятия денег и перевода денег между счетами.
3. Бонусное задание
Реализуйте способ хранения и печати истории транзакций для каждого счета.

Ограничения
Не используйте классы или словари.
Используйте только базовые конструкции Python, такие как def, lists, if, elif и else.

"""

accounts = []
transactions = []

def create_account(name, initial_balance):
    """Создает новый счет с начальным балансом."""
    account = [name, initial_balance]
    accounts.append(account)
    print(f"Счет '{name}' создан с начальным балансом: {initial_balance}")

def deposit(account_name, amount):
    """Вносит деньги на счет."""
    for account in accounts:
        if account[0] == account_name:
            account[1] += amount
            transactions.append(f"Депозит: {amount} на счет '{account_name}'")
            print(f"На счет '{account_name}' внесено: {amount}")
            return
    print(f"Счет '{account_name}' не найден.")

def withdraw(account_name, amount):
    """Снимает деньги со счета."""
    for account in accounts:
        if account[0] == account_name:
            if account[1] >= amount:
                account[1] -= amount
                transactions.append(f"Снятие: {amount} со счета '{account_name}'")
                print(f"С счета '{account_name}' снято: {amount}")
            else:
                print(f"Недостаточно средств на счете '{account_name}'. Текущий баланс: {account[1]}")
            return
    print(f"Счет '{account_name}' не найден.")

def check_balance(account_name):
    """Проверяет текущий баланс счета."""
    for account in accounts:
        if account[0] == account_name:
            print(f"Текущий баланс счета '{account_name}': {account[1]}")
            return
    print(f"Счет '{account_name}' не найден.")

def transfer(from_account, to_account, amount):
    """Переводит деньги между счетами."""
    for account in accounts:
        if account[0] == from_account:
            if account[1] >= amount:
                account[1] -= amount
                transactions.append(f"Перевод: {amount} с '{from_account}' на '{to_account}'")
                for target_account in accounts:
                    if target_account[0] == to_account:
                        target_account[1] += amount
                        print(f"Переведено {amount} с '{from_account}' на '{to_account}'")
                        return
                print(f"Счет '{to_account}' не найден.")
                account[1] += amount  # Возвращаем обратно
                return
            else:
                print(f"Недостаточно средств на счете '{from_account}'. Текущий баланс: {account[1]}")
            return
    print(f"Счет '{from_account}' не найден.")

def print_transactions():
    """Печатает историю транзакций."""
    if transactions:
        print("История транзакций:")
        for transaction in transactions:
            print(transaction)
    else:
        print("История транзакций пуста.")

def main():
    create_account("Alice", 1000)
    create_account("Bob", 500)

    deposit("Alice", 200)
    withdraw("Bob", 100)
    check_balance("Alice")
    check_balance("Bob")

    transfer("Alice", "Bob", 300)
    check_balance("Alice")
    check_balance("Bob")

    print_transactions()

if __name__ == "__main__":
    main()

""">Комментарии от преподавателя:

>Задание сгенерированно нейросетью, подойти к преподавателю для защиты данного задания
"""
