# pythonProject 10

# Бот на aiogram, ведущий телеграм-группу с рецептами

# По нажатию кнопки бот присылает случайный рецепт в личку.
# Осуществляет поиск рецепта запросу пользователя "пирог с курицей" или "яйца колбаса майонез".
# Добавляет в текст рецепта рекламу.
# Используем HTML-разметку, жирный шрифт, курсив, emoji - украшаем посты

# $ pip install schedule - установить внешние зависимости

import random
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

try:
    # Загружаем список с рекламными объявлениями из файла promotions.txt
    try:  # этот блок не прерывает работу программы
        p = open('promotions.txt', 'r', encoding='UTF-8')
        prom_list = p.read().split('\n\n\n')
    finally:
        p.close()  # и закрывает открытый файл если он не прочитался
except FileNotFoundError:
    print("Невозможно открыть файл promotions.txt")
except:
    print("Ошибка при работе с файлом promotions.txt")

try:
    # список с путями к рецептам
    path_list = ['rec1/recipes1.txt', 'rec1/recipes2.txt', 'rec1/recipes3.txt', 'rec1/recipes4.txt',
                 'rec1/recipes5.txt', 'rec1/recipes6.txt', 'rec1/recipes7.txt', 'rec1/recipes8.txt',
                 'rec1/recipes9.txt', 'rec1/recipes10.txt', 'rec2/recipes11.txt', 'rec2/recipes12.txt',
                 'rec2/recipes13.txt', 'rec2/recipes14.txt', 'rec2/recipes15.txt', 'rec2/recipes16.txt',
                 'rec2/recipes17.txt', 'rec2/recipes18.txt', 'rec2/recipes19.txt', 'rec2/recipes20.txt',
                 'rec3/recipes21.txt', 'rec3/recipes22.txt', 'rec3/recipes23.txt', 'rec3/recipes24.txt',
                 'rec3/recipes25.txt', 'rec3/recipes26.txt', 'rec3/recipes27.txt', 'rec3/recipes28.txt',
                 'rec3/recipes29.txt', 'rec3/recipes30.txt', 'rec4/recipes31.txt', 'rec4/recipes32.txt',
                 'rec4/recipes33.txt', 'rec4/recipes34.txt',
                 'rec4/recipes35.txt', 'rec4/recipes36.txt', 'rec4/recipes37.txt', 'rec4/recipes38.txt',
                 'rec4/recipes39.txt', 'rec4/recipes40.txt', 'rec4/recipes41.txt', 'rec4/recipes42.txt',
                 'rec5/recipes43.txt', 'rec5/recipes44.txt', 'rec5/recipes45.txt', 'rec5/recipes46.txt',
                 'rec5/recipes47.txt', 'rec5/recipes48.txt', 'rec5/recipes49.txt', 'rec5/recipes50.txt',
                 'rec5/recipes51.txt', 'rec5/recipes52.txt', 'rec5/recipes53.txt', 'rec5/recipes54.txt']
    r_list = []  # Список списков с рецептами

    # Загружаем список рецептов1
    for path_recipes in path_list:
        try:
            f = open(path_recipes, 'r', encoding='UTF-8')
            r_list.append(f.read().split('\n\n\n'))
        finally:
            f.close()
except FileNotFoundError:
    print(f"Невозможно открыть файл: {path_list[len(r_list)]}")
except:
    print(f"Ошибка при работе с файлами {path_list[len(r_list)]}")

print(f"загружено {len(r_list)} файлов")

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):  # функция принимает (_) аргумент!
    """Выполняется при включении бота"""
    print("Бот работает")


# Команда start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    """
    По команде создает кнопку "Рецепт" чате (в личке или группе) и выводит приветственное сообщение
    :param message: /start
    :return:
    """
    # Добавляем кнопку
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рецепт")
    markup.add(item1)
    await bot.send_message(message.chat.id,
                           'Нажми: \n"Рецепт", чтобы получить случайный рецепт или "Пирог из яблок", если Вы ищете какое-то конкретное блюдо',
                           reply_markup=markup)


@dp.message_handler()
async def send_hello(message: types.Message):
    """
    Бот на bot.send_message() - отправляет пользователю HELLO:
    если chat_id=message.chat.id:
        в чат - если пользователь написал в чат
        в личку - если пользователь написал боту
    если chat_id=message.from_user.id:
        в личку пользователю - в любом случае
    """
    await bot.send_message(chat_id=message.chat.id,
                           text='HELLO')  # =id чата, куда пришло сообщение
    # await bot.send_message(chat_id=message.from_user.id, text='HELLO')  # =id чата пользователя, приславшего сообщение


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
    # прописываем аргумент on_startup=on_startup, чтобы функция on_startup(_) выполнялась при включении бота
