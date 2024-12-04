

# Задание 1

Задача: Создать чат бота для получения информации об исследованиях космоса

Описание: Создайте комплексное приложение командной строки, которое будет использоваться в качестве панели управления исследованиями космоса. Данное приложение будет обращаться к https://api.nasa.gov/ для предоставления пользователям набора информации о космосе, включая:

- Астрономическая картинка дня (APOD): Отображение APOD с пояснениями к нему.
- Фотографии с марсохода: позволяет пользователям выбирать и фильтровать фотографии с марсохода по дате и типу камеры.
- Объекты, сближающиеся с Землей (ОСЗ): Поиск и отображение информации об объекте, сближающихся с Землей, на определенную дату, включая их размеры и потенциальную опасность.
- Данные о космической погоде: Отображают последние данные о космической погоде, включая солнечные вспышки и геомагнитные бури.
Приложение должно позволять пользователям ориентироваться в этих функциях, корректно обрабатывать ошибки и обеспечивать удобство работы.

Требования:
- Пользовательский ввод: Приложение должно предложить пользователю ввести данные, чтобы выбрать, какую функцию он хочет изучить.
- Проверка данных: Убедитесь, что пользовательские данные (например, даты) проверены.
- Обработка ошибок: Корректно обрабатывайте ошибки API и неверные ответы.
- Представление данных: Представляйте данные в четкой и организованной форме.
- Опция выхода: позволяет пользователям выходить из приложения в любое время.
"""

import requests

api_key = ""


def get_apod():
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}')
    if response.status_code == 200:
        data = response.json()
        if 'title' in data and 'url' in data:
            print("Изображение:", data['title'])
            print("Дата:", data['date'])
            print("Описание:", data['explanation'])
            print("Ссылка на изображение:", data['url'])
        else:
            print("Некорректные данные от API")
    else:
        print("Ошибка при получении изображения")


def get_mars_photo():
    sol = input("Введите сол")
    camera = input('Введите тип камеры !НЕОБЯЗАТЕЛЬНО!')
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key={api_key}"
    if camera:
        url += f"&camera={camera}"

    response = requests.get(url)
    if response.status_code == 200:
        photos = response.json().get('photos', [])
        for photo in photos[:1]:
            if photos:
                print(photo['img_src'])
            else:
                print('Нет фото для вашего запроса')

    else:
        print('Ошибка при получении данных для фото', response.status_code)


def get_neo():
    date = input('Введите дату (YYYY-MM-DD):')
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date}E&end_date={date}&api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        neos = response.json().get('near_earth_objects', {}).get(date, [])
        if neos:
            for obj in neos:
                print('Название:', obj['name'])
                print('Размер:', obj['estimated_diameter'])
                print('Потенциальная опасность:', obj['is_potentially_hazardous_asteroid'])
        else:
            print('Объектов нету')
    else:
        print('Ошибка')


def get_space_weather():
    url = f"https://api.nasa.gov/DONKI/FLR?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        flares = response.json()
        if flares:
            for flare in flares[:5]:
                print('Событие:', flare['flrID'])
                print('Время начала:', flare['beginTime'])
                print('Время пика:', flare['peakTime'])
                print('Тип:', flare['classType'])
        else:
            print('Нет данных')
    else:
        print('Ошибка')


def main():
    while True:
        print("Выберите, что хотите узнать:")
        print("1. Космическая картинка APOD")
        print("2. Фотография с марсохода")
        print("3. Объекты, сближающиеся с Землей (ОСЗ)")
        print("4. Данные о космической погоде")
        print("5. ВЫХОД")

        choice = input('')

        if choice == "1":
            get_apod()
        elif choice == "2":
            get_mars_photo()
        elif choice == "3":
            get_neo()
        elif choice == "4":
            get_space_weather()
        else:
            print('Выход соверешен')
            break


main()

"""# Задание 2

Описание задачи

Цель этой задачи - создать скрипт на Python, который взаимодействует с API Чикагского института искусств (https://api.artic.edu/docs/) для извлечения и отображения произведений искусства. Скрипт должен позволять пользователям просматривать работы по страницам, фильтровать их по имени художника и просматривать подробную информацию о выбранных произведениях искусства. Ниже приведены требования и функциональные возможности, которые необходимо реализовать:

Требования:
Извлекать произведения искусства:

- Создайте функцию, которая извлекает список произведений искусства из API Чикагского института искусств.
Функция должна принимать параметр page для разбивки на страницы и возвращать список произведений искусства вместе с информацией о разбивке на страницы.
Фильтровать произведения искусства:

- Реализуйте функцию, которая фильтрует список произведений искусства на основе имени указанного художника. Функция должна возвращать список работ, которые соответствуют имени художника (без учета регистра).
Отображать подробную информацию об оформлении:

- Напишите функцию, которая отображает названия работ для пользователя и позволяет ему выбрать одну из них, введя соответствующий номер.
После выбора функция должна отображать подробную информацию о выбранном произведении, включая название, исполнителя, дату и носитель.
Разбивка на страницы и взаимодействие с пользователем:

- Создайте основную функцию, которая управляет выборкой произведений и взаимодействием с пользователем.

Разрешите пользователям перемещаться по страницам с произведениями искусства, выполнять фильтрацию по исполнителю или выходить из программы.

Если страниц с произведениями искусства несколько, укажите варианты перехода к следующей странице, предыдущей странице, фильтрации по исполнителю или выхода из программы.
"""

import requests


def fetch_artworks(page=1):
    url = f'https://api.artic.edu/api/v1/artworks?page={page}&limit=10'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', []), data.get('pagination', {})
    else:
        print("Не удалось получить данные")
        return [], {}


def filter_artworks_by_artist(artworks, artist_name):
    return [art for art in artworks if 'artist_title' in art and artist_name.lower() in art['artist_title'].lower()]


def show_artwork_details(artwork):
    print("\nИнформация о выбранном произведении:")
    print("Название:", artwork.get('title', 'Неизвестно'))
    print("Автор:", artwork.get('artist_title', 'Неизвестен'))
    print("Дата:", artwork.get('date_display', 'Не указана'))
    print("Материал:", artwork.get('medium_display', 'Не указан'))
    print("\n")


def main():
    page = 1
    while True:
        artworks, pagination = fetch_artworks(page)
        print(f"\nСтраница {page}")
        for i, art in enumerate(artworks, start=1):
            print(f"{i}. {art.get('title', 'Без названия')}")

        choice = input("1. Подробности"
                       "\n2. Следущая страница"
                       "\n3. Предыдущая страница"
                       "\n4. Фильтр по художнику"
                       "\n5. Выйти"
                       "\nВаш выбор: ")

        if choice == '1':
            index = int(input("Введите номер произведения: ")) - 1
            if 0 <= index < len(artworks):
                show_artwork_details(artworks[index])
            else:
                print("Неверный номер")

        elif choice == '2':
            page += 1

        elif choice == '3':
            page = max(1, page - 1)

        elif choice == '4':
            artist_name = input("Введите имя художника:")
            filtered_artworks = filter_artworks_by_artist(artworks, artist_name)
            if filtered_artworks:
                for i, art in enumerate(filtered_artworks, start=1):
                    print(f"{i}. {art.get('title', 'Без названия')}")
                index = int(input("Введите номер для подробностей:")) - 1
                if 0 <= index < len(filtered_artworks):
                    show_artwork_details(filtered_artworks[index])
            else:
                print("Нет произведений для этого художника")

        elif choice == '5':
            break

        else:
            print("Неверный ввод")


main()

"""# Задание 3

Задача: Создать программу по управлению портфелем криптовалют

Цель: Создать скрипт на Python, который извлекает цены на криптовалюты в режиме реального времени, позволяет пользователям управлять портфелем криптовалют, вычисляет общую стоимость портфеля, отслеживает изменения цен и предоставляет исторические данные о ценах для анализа.

Требования:
Получение текущих цен на криптовалюты:

Используйте https://docs.coingecko.com/ для получения актуальных цен на список криптовалют.

Управление портфелем:

- Позволяет пользователю создавать портфель криптовалют и управлять им, указывая количество каждой криптовалюты, которой он владеет.
- Расчитывает общую стоимость портфеля в указанной фиатной валюте (например, долларах США).

Отслеживание изменения цен:

- Отображение процентного изменения цены для каждой криптовалюты в портфеле за последние 24 часа.
- Выделите все криптовалюты, стоимость которых значительно увеличилась или снизилась.

Поиск исторических данных о ценах:

- Получение исторических данных о ценах на указанную криптовалюту за последнюю неделю.
- Предоставьте пользователю возможность визуализировать эти данные в простом текстовом формате (например, цены за день).

Взаимодействие с пользователем:

- Реализуйте интерфейс командной строки для ввода данных пользователем.
- Предоставьте опции для получения текущих цен, управления портфелем, просмотра изменений цен или анализа исторических данных.
"""



"""# Дополнительно: Задание 4

Задание 4: Проектное

Вам необходимо самостоятельно найти откртое API предоставляющее информацию в открытом доступе и реализовать собственный проект!


Критерии приемки результата:

- Проект включает в себя не менее 5 возможостей для пользователя
- Проект позволяет использовать все возможности проекта пользователю при помощи взаимодействия через коммандную строку
- Проект работает с открытым API (это значит что при проверке вашей работы преподавателем, преподавателю необходимо просто запустить ячейку с кодом вашего проекта и она будет работать без дополнительных манипуляции)
- Проект должен обязательно включать в себя ряд используемых конструкции:
    - Функции
    - Условные конструкции
    - Ввод/вывод
    - Словари/Списки
- Допускается использование библиотек:
    - requests
    - datetime
    - random

**Здесь добавьте описание вашего проекта**
"""

#  А здесь код
