

"""## Задание 1. HTTP-запросы, ответы и погода

Описание:

Напишите HTTP-запрос для получения информации о погоде в введенном городе из API.

Можно использовать API: https://open-meteo.com/. Используйте метод GET.


Ввод
```
56.50, 60.35
```

Вывод
```
Сегодня (1.11) погода 20 ◦С, нет осадков, туман
```
"""

import requests
from datetime import datetime


def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(
        lon) + "&current_weather=true"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        current_weather = data.get("current_weather", {})
        temperature = current_weather.get("temperature", "N/A")
        precipitation = current_weather.get("precipitation", 0)
        visibility = current_weather.get("visibility", 10000)

        today = datetime.now()
        date_today = today.strftime("%d.%m")

        if precipitation == 0:
            precipitation_text = "нет осадков"
        else:
            precipitation_text = "есть осадки"

        if visibility < 1000:
            visibility_text = "туман"
        else:
            visibility_text = "ясно"

        print("Сегодня (" + date_today + ") погода " + str(
            temperature) + " ◦С, " + precipitation_text + ", " + visibility_text)
    else:
        print("Не удалось получить данные о погоде")


latitude = input("Введите широту: ")
longitude = input("Введите долготу: ")

get_weather(float(latitude), float(longitude)

""">Комментарии от преподавателя:
- Отсуствует ввод в программе

## Задание 2. HTTP-запросы, ответы и покемоны

**Описание:**


Создайте код программы, которая будет взаимодействовать с API, со следующим функионалом:

1. Используя метод GET, отправьте запрос на endpoint /pokemon, чтобы получить список первых 20 покемонов

2. Извлеките имена покемонов из ответа и выведите их списком

3. Введите с помощью input() название одного из покемонов


```
Имя покемона: clefairy
```



4. Отправьте GET-запрос, чтобы получить полную информацию о выбранном покемоне

5. Извлеките и выведите следующие данные о введенном покемоне:

     • Имя

     • Тип

     • Вес

     • Рост

     • Способности

Используйте PokéAPI (https://pokeapi.co/), который предоставляет информацию о покемонах, их характеристиках, типах и другую информацию.
"""

import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=52"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pokemons = data["results"]

    print("Список покемонов:")
    for pokemon in pokemons:
        print(pokemon["name"])
else:
    print("Ошибка при получении списка покемонов")

pokemon_name = input("Введите имя одного из покемонов: ")

url_pokemon = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
response_pokemon = requests.get(url_pokemon)

if response_pokemon.status_code == 200:
    data_pokemon = response_pokemon.json()

    name = data_pokemon["name"]
    types = [type_info["type"]["name"] for type_info in data_pokemon["types"]]
    weight = data_pokemon["weight"]
    height = data_pokemon["height"]
    abilities = [ability["ability"]["name"] for ability in data_pokemon["abilities"]]

print('Имя', name)
print('Тип', types)
print('Вес', height)
print('Рост', weight)
print('Способности', abilities)

"""## Задание 3. HTTP-запросы, ответы и посты

**Описание:**

Создайте программу, которая будет взаимодействовать с JSONPlaceholder API, реализуя следующие функции:

1. Реализуйте функцию, которая выполняет GET-запрос к https://jsonplaceholder.typicode.com/posts и возвращает список постов в формате JSON

2. Реализуйте функцию, котороая получает вводимое ID поста, выполняет GET-запрос по ID и возвращает данные поста в формате JSON

3. Реализуйте функцию, которая выполняет обработку JSON из пункта 2 и выводит всю важную информацию в консоль
"""

import requests


def get_all_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts_data = response.json()
        return posts_data
    else:
        print("Не удалось получить список постов")
        return []


def get_post_by_id(post_id):
    url = "https://jsonplaceholder.typicode.com/posts/" + str(post_id)
    response = requests.get(url)

    if response.status_code == 200:
        post_data = response.json()
        return post_data
    else:
        print("Не удалось получить пост с ID:", post_id)
        return None


def print_post_details(post_data):
    if post_data:
        print("ID поста:", post_data.get("id"))
        print("ID пользователя:", post_data.get("userId"))
        print("Заголовок поста:", post_data.get("title"))
        print("Текст поста:", post_data.get("body"))
    else:
        print("Нет данных для отображения.")


all_posts = get_all_posts()
print("Количество постов:", len(all_posts))

post_id_input = input("Введите ID поста, который хотите посмотреть: ")
single_post_data = get_post_by_id(post_id_input)

print("Детали поста:")
print_post_details(single_post_data)

"""## Задание 4. HTTP-запросы, ответы и работа с постами

**Описание**

Создайте программу, которая будет взаимодействовать с JSONPlaceholder API (из предыдущего задания), реализуя новые функции:

1. Реализуйте функцию, которая принимает заголовок, содержимое и ID пользователя (информация вводится с помощью input()), выполняет POST-запрос для создания нового поста и возвращает информацию о созданном посте в формате JSON


```
Заголовок: Новый пост
Содержимое поста: Тут должно находиться содержимое нового поста...
ID пользователя: 10
```



2. Реализуйте функцию, которая принимает ID поста, новый заголовок и новое содержимое, выполняет PUT-запрос и возвращает обновлённый пост в формате JSON

3. Реализуйте функцию, которая принимает ID поста, выполняет DELETE-запрос и возвращает статус-код ответа
"""

import requests


def create_post():
    title = input("Введите заголовок поста: ")
    body = input("Введите содержимое поста: ")
    user_id = input("Введите ID пользователя: ")

    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    response = requests.post(url, json=data)

    if response.status_code == 201:
        created_post = response.json()
        return created_post
    else:
        print("Не удалось создать новый пост")
        return None


def update_post(post_id):
    new_title = input("Введите новый заголовок поста: ")
    new_body = input("Введите новое содержимое поста: ")

    url = "https://jsonplaceholder.typicode.com/posts/" + str(post_id)
    data = {
        "title": new_title,
        "body": new_body
    }

    response = requests.put(url, json=data)

    if response.status_code == 200:
        updated_post = response.json()
        return updated_post
    else:
        print("Не удалось обновить пост с ID:", post_id)
        return None


def delete_post(post_id):
    url = "https://jsonplaceholder.typicode.com/posts/" + str(post_id)

    response = requests.delete(url)

    if response.status_code == 200:
        print("Пост успешно удален.")
    else:
        print("Не удалось удалить пост с ID:", post_id)

    return response.status_code


new_post = create_post()
if new_post:
    print("Новый пост создан:", new_post)

post_id_to_update = input("Введите ID поста, который хотите обновить: ")
updated_post = update_post(post_id_to_update)
if updated_post:
    print("Обновленный пост:", updated_post)

post_id_to_delete = input("Введите ID поста, который хотите удалить: ")
delete_status = delete_post(post_id_to_delete)
print("Статус удаления:", delete_status)

"""## Задание 5. HTTP-запросы, ответы и пёсики

**Описание**

Создайте программу, которая будет взаимодействовать с Dog API, которая позволит получать список пород собак, вводить несколько пород и получать их фотогрфии.

Этапы:

1. Создайте функцию, которая использует метод GET и возвращает список всех пород собак в формате нумерованного списка

2. Реализуйте возможность ввода нескольких пород собак через запятую


```
african, chow, dingo
```



3. Создание функции, которая реализует запрос, возвращает и выводит изображениия собак, породы которых были введены до этого


Используйте Dog API (https://dog.ceo/dog-api/), который предоставляет информацию о породах собак и их изображения.
"""

import requests


def get_all_dog_breeds():
    dog_api_url = "https://dog.ceo/api/breeds/list/all"
    breed_response = requests.get(dog_api_url)

    if breed_response.status_code == 200:
        json_data = breed_response.json()
        all_breeds_dictionary = json_data["message"]
        breed_list = []

        for key in all_breeds_dictionary:
            breed_list.append(key)

        print("Список всех пород собак:")
        count = 1
        for breed in breed_list:
            print(str(count) + ". " + breed)
            count += 1

        return breed_list
    else:
        print("Ошибка при получении списка пород собак")  # если что-то пошло не так
        return []


def get_dog_images_by_breeds(breeds_input_text):
    breeds_split_list = breeds_input_text.split(",")
    breeds_cleaned_list = []

    for breed in breeds_split_list:
        cleaned_breed = breed.strip()
        breeds_cleaned_list.append(cleaned_breed)

    for single_breed in breeds_cleaned_list:
        breed_image_url = "https://dog.ceo/api/breed/" + single_breed + "/images/random"
        breed_image_response = requests.get(breed_image_url)

        if breed_image_response.status_code == 200:
            image_data = breed_image_response.json()
            dog_image_url = image_data["message"]

            print("Фото для породы " + single_breed + ": " + dog_image_url)
        else:
            print("Не удалось получить фото для породы: " + single_breed)


all_breeds_list = get_all_dog_breeds()

print("Введите породы собак, которые хотите увидеть, через запятую (например, african, chow, dingo):")
user_breeds_input = input()

get_dog_images_by_breeds(user_breeds_input)
