# pythonProject9

[Ru] БОТ, ВЕДУЩИЙ TELEGRAM-КАНАЛ С РЕЦЕПТАМИ

## Описание

#### Бот получает список рецептов из файла, создает словарь и рецепты по очереди (с рекламой!!!) и с фото блюда через случайные период времени постит в канал.

## Требования

* Установить внешние зависимости
* $ pip install -r requirements.txt
* Создать свой канал в Telegram, добавить в подписчики канала нашего бота и назначить его администратором канала с
  правом публиковать сообщения.
* Создать файлы с рецептами (recipes1.txt, recipes2.txt...) и размесить в папке со скриптом бота.
* Создать папки с фото блюд (pictures1, pictures2...)
* Создать файл promotions.txt со списком реклам
* Создать файл config.py, в котором будут храниться токен для доступа к боту и адрес телеграм-канала (начинается с @) в
  виде

```python
token = "1234567890:ASDFGHH..."
channel = '@topjokes...'
```

## Где взять токен?

* https://xakep.ru/2021/11/28/python-telegram-bots/

## Подключаем модули

```python
import telebot
import random
import time
import datetime
from config import token, channel
```

## Примеры использования

#### Загружает список с текстом из файла, выводит уведомление об удачной загрузке или ошибке

Указываем название текстового файла с рецептами, 'r' - чтение текста, кодировку текта 'UTF-8'
Рецепты в текстовом файле разделены двумя пустыми строками (\n\n\n)

```python
def open_text(path):
    try:
        # Загружаем список с текстом из файла
        try:  # этот блок не прерывает работу программы
            p = open(path, 'r', encoding='UTF-8')
            text_list = p.read().split('\n\n\n')
            print(f"Загружен файл \"{path}\" длиной {len(text_list)}")
        finally:
            p.close()  # и закрывает открытый файл если он не прочитался
    except FileNotFoundError:
        print(f"Невозможно открыть текстовый файл: {path}")
    except:
        print(f"Ошибка при работе с текстовым файлом: {path}")
    return text_list
```

#### Для удобства работы преобразуем списоки с рецептами в словари

```python
def convert_to_dict(recipe_list):
    d_recipes = {}
    for recipe in recipe_list:
        d_recipes[recipe[:recipe.index("\n\n")]] = recipe
    return d_recipes
```

#### Тестовая функция

Перебирает все блюда. Стабильно обрабатывает 10-20 сообщений (использовать срезы списков). Выводит название блюда и
длину сообщения

```python
def test():
    for recipe_name in recipe_names5:  # МЕНЯТЬ recipe_names1
        # Перебирем все блюда. Если выводит ошибку - попрововать сделать срез списка
        time.sleep(2)
        promo = random.choice(prom_list)  # реклама
        print(f"recipe_name: {recipe_name}, promo: {promo}")
        answer = d5_recipes[recipe_name]  # МЕНЯТЬ d1_recipes
        # выбираем рецепт из словаря по названию блюда
        if len(answer + '\n\n' + promo) < 1000:
            answer += '\n\n' + promo

        print("длина рецепта: ", len(answer))  # если длина более 1024, то картинку не закрепить
        try:
            try:  # этот блок не прерывает работу программы
                files = open(path_dict5[recipe_name], 'rb')  # МЕНЯТЬ path_dict1
                # открываем картинку
                bot.send_photo(CHANNEL_NAME, photo=files, caption=answer)  # посылаем ее и рецепт
            finally:
                files.close()  # и закрывает открытый файл если он не прочитался
        except FileNotFoundError:
            print("Невозможно открыть файл с изображением")
        except:
            print("Ошибка при работе с изображением")
```

#### Определяет из какой папки будут браться рецепты. Возвращает: словарь с рецептами, список с названиями блюд, словарь с путями к фото

```python
def get_path(ind):
    # ind = random.randint(1, 5)  # случайным образом
    if ind == 1:
        d_rec = d1_recipes
        recipe_n = recipe_names1
        path_d = path_dict1
    elif ind == 2:
        d_rec = d2_recipes
        recipe_n = recipe_names2
        path_d = path_dict2
    else:
        d_rec = d5_recipes
        recipe_n = recipe_names5
        path_d = path_dict5
    return d_rec, recipe_n, path_d
```

#### Загружаем список с рекламными объявлениями и рецепты из файлов, создаем словарь с рецептами и список названий блюд

```python
prom_list = open_text('promotions.txt')
recipes1 = open_text('recipes1.txt')
d1_recipes = convert_to_dict(recipes1)  # словарь1 с рецептами
recipe_names1 = list(d1_recipes.keys())  # список1 с названиями блюд
```

#### Cписок1 с путями к фото {"название блюда":"путь к нему"}

```python
path_dict1 = {"Фриттaтa c xлeбoм": "pictures1/pict1.jpg", 'Твoрoжный cмузи c бaнaнoм и кaкao': "pictures1/pict2.jpg"}
```

#### Выставляем время начала работы бота "morning" и окончания "night", чтобы сообщения не будили по ночам

```python
work_bot_fl = True
while work_bot_fl:
    current_date_time = datetime.datetime.now()
    now = current_date_time.time()  # текущее время
    morning = datetime.time(7, 32, 0)  # время начала работы бота
    night = datetime.time(12, 45, 0)  # время окончания работы бота
```

#### Посылаются рецепты по порядку через случайные периоды времени в диапазоне от 1  до 5 часов

```python
        if morning < now < night:  # если день
    number_dict = int(*open_text('number_dict.txt'))  # номер словаря
number_recipe = int(*open_text('number_recipe.txt'))  # номер рецепта

d_recipes, recipe_names, path_dict = get_path(number_dict)
# словарь с рецептами, список с названиями блюд, словарь с путями к фото

print(f"Бот работает, папка с рецептами: {number_dict}, рецепт номер: {number_recipe}")  # проверка бота
time.sleep(random.randint(60, 7200))  # c 7 до 9 самое популярное время для постов
promo = random.choice(prom_list)  # реклама
recipe_name = recipe_names[number_recipe]  # название блюда
answer = d_recipes[recipe_name]  # выбираем рецепт из словаря по названию блюда

if len(answer + '\n\n' + promo) < 1000:  # если длиннее, то картинка не прикрепится, ограничение телеграмм
    answer += '\n\n' + promo
try:
    try:  # этот блок не прерывает работу программы
        files = open(path_dict[recipe_name], 'rb')  # открываем картинку
        bot.send_photo(CHANNEL_NAME, photo=files, caption=answer)  # посылаем ее и рецепт
    finally:
        files.close()  # и закрывает открытый файл если он не прочитался
except FileNotFoundError:
    print("Невозможно открыть файл с изображением")
except:
    print("Ошибка при работе с изображением")

try:  # перебираем рецепты
    if number_recipe < len(recipe_names) - 1:
        # [0,1,2,3] len ==4 => 2 - предпоследний номер и может быть еще увеличен
        number_recipe += 1
    else:
        number_recipe = 0
        number_dict += 1
        try:  # этот блок переключает словарь
            file = open("number_dict.txt", "w")  # открываем НЕ писать кодировку?
            file.write(f"{number_dict}")
        finally:
            file.close()  # и закрывает открытый файл если он не прочитался
    try:  # этот блок переключает рецепт
        file = open("number_recipe.txt", "w")  # открываем НЕ писать кодировку?
        file.write(f"{number_recipe}")
    finally:
        file.close()  # и закрывает открытый файл если он не прочитался
except FileNotFoundError:
    print("Невозможно открыть файл с номером")
except:
    print("Ошибка при работе с файлом с номером")

# таймер работы бота (от 1 до 5 часов)
time.sleep(random.randint(3600, 17000))  # один-два поста в день достаточно для дзен
```
