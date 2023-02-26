# pythonProject 10

# Бот на aiogram, ведущий телеграм-канал с рецептами
# Бот получает список рецептов из файла, создает словарь и рецепты по очереди (с рекламой!!!) и с фото блюда
# через случайные период времени постит в канал
# Для этого нам нужно создать свой канал в Telegram,
# добавить в подписчики канала нашего бота и назначить его администратором канала с правом публиковать сообщения.
# Файлы с рецептами должен лежать рядом со скриптом бота.
# Папки с фото должны лежать рядом со скриптом бота.
# Используем HTML-разметку, жирный шрифт, курсив, emoji - украшаем посты

# $ pip install schedule - установить внешние зависимости

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):  # функция принимает (_) аргумент!
    """Выполняется при включении бота"""
    print("Бот работает")


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
