from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
import sqlite3

bot = Bot('******************')
dp = Dispatcher(bot)

conn = sqlite3.connect('candies.db')
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS test (
#                 test PRIMARY KEY,
#                 user_id,
#                 user_name text,
#                 user_surname text,
#                 username text,
#                 candy_left text)''')
print("Подключен к БД")


def write_db(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('''INSERT or IGNORE INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)''',
                   (user_id, user_name, user_surname, username))
    conn.commit()


def update_db(message, count):
    sql_update = f"UPDATE test SET candy_left = candy_left - {count} WHERE user_id == {message.from_user.id}"
    cursor.execute(sql_update)
    conn.commit()


def start(message):
    sql_update = f"UPDATE test SET candy_left = 99 WHERE user_id == {message.from_user.id}"
    cursor.execute(sql_update)
    conn.commit()


def candies(message):
    candy = f'SELECT candy_left FROM test WHERE user_id == {message.from_user.id}'
    cursor.execute(candy)
    candy_left = cursor.fetchall()
    conn.commit()
    return candy_left[0][0]


@dp.message_handler(content_types='text')
async def chat_id(message):
    p1 = message.text
    p2 = 0
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    if message.text == '/start':
        start(message)
        await message.reply(f'Игра начата! Вы можете взять от 1 до 28 конфет, победит тот,'
                            f' кто последний заберет конфеты, всего 101 конфета\n'
                            f'\nБерите конфеты:')
        write_db(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
    if p1.isdigit():
        candy = candies(message)
        if int(p1) < 1 or int(p1) > 28:
            await message.reply(f"Вы можете взять от 1 до 28 конфет\n"
                                )
        elif int(p1) > int(candy):
            await message.reply(f"Вы не можете взять больше конфет, чем осталось\n"
                                f"\n{candy} осталось\n")
        else:
            candy -= int(p1)
            update_db(message, p1)
            pn = 1
            if candy != 0:
                if candy % 29 != 0:
                    while (candy - p2) % 29 != 0:
                        p2 = random.randint(1, 28)
                    while p2 > candy and (candy - p2) % 29 != 0:
                        p2 = random.randint(1, 28)
                    while int(p2) <= 0 and (candy - p2) % 29 != 0 or int(p2) > 28 and (candy - p2) % 29 != 0:
                        p2 = random.randint(1, 28)
                        while p2 > candy and (candy - p2) % 29 != 0:
                            p2 = random.randint(1, 28)
                else:
                    while p2 > candy:
                        p2 = random.randint(1, 28)
                    while int(p2) <= 0 or int(p2) > 28:
                        p2 = random.randint(1, 28)
                        while p2 > candy:
                            p2 = random.randint(1, 28)
                await message.reply(f"\n{candy} осталось\n"
                                    f"\nBot взял {p2}")
                candy -= p2
                update_db(message, p2)
                pn = 2
                if candy != 0:
                    await message.reply(f"\n{candy} осталось\n"
                                        f"\nБерите конфеты:")
                else:
                    await message.reply(f"\n{candy} осталось\n")
                    if pn == 1:
                        await message.reply('\n---------\n'
                                            'Вы победили\n'
                                            '-----------\n')
                    else:
                        await message.reply('\n---------\n'
                                            'Bot победил\n'
                                            '-----------\n')
            else:
                await message.reply(f"\n{candy} осталось\n")
                if pn == 1:
                    await message.reply('\n---------\n'
                                        'Вы победили\n'
                                        '-----------\n')
                else:
                    await message.reply('\n---------\n'
                                        'Bot победил\n'
                                        '-----------\n')
    else:
        write_db(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)


print('Погнали')
executor.start_polling(dp)
