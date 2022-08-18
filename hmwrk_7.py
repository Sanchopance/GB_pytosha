import sys
import sqlite3


def print_menu():
    print('\nВыберите, что будем делать:')
    print('1. Добавить контакт')
    print('2. Отобразить контакты')
    print('3. Изменить контакт')
    print('4. Удалить контакт')
    print('5. Найти контакт')
    print('0. Выход')


def addcontact():
    while True:
        name = input("Имя контакта: ")
        if len(name) != 0:
            break
        else:
            print("Введите имя")
    while True:
        surname = input("Фамилия контакта: ")
        if len(surname) != 0:
            break
        else:
            print("Введите фамилию")
    while True:
        num = input("Номер телефона: ")
        if not num.isdigit():
            print("Введите номер")
            continue
        elif len(num) > 18:
            print("Введите номер, без всякой ерунды, только цифры")
            continue
        else:
            break
    cursor.execute('''INSERT INTO phonebook (name, surname, phone_number) VALUES (?,?,?)''',
                   (name, surname, num))
    conn.commit()
    print("Новый контакт " + name + ' ' + surname + " добавлен в нашу телефонную книгу")


def displaybook():
    cursor.execute("SELECT surname, name, phone_number FROM phonebook ORDER BY surname")
    results = cursor.fetchall()
    print(results)


def key_pair_reception(str):
    print("\nВыберите что менять")
    print('1. Имя')
    print('2. Фамилия')
    print('3. Номер телефона')
    print('0. Вернуться в меню')
    n = int(input('Выбираем: '))
    if n == 1:
        field = "name"
    elif n == 2:
        field = "surname"
    elif n == 3:
        field = "phone_number"
    else:
        return None
    keyword = input("\nВведите имя контакта: " + field + " = ")
    keypair = field + "='" + keyword + "'"
    return keypair


def editcontacts():
    s = key_pair_reception('searching')
    u = key_pair_reception('updating')
    if s != None:
        sql = "UPDATE phonebook SET " + u + " WHERE " + s
        cursor.execute(sql)
        conn.commit()
        print("Внесли изменения в " + s + ".\n")


def deletecontacts():
    s = key_pair_reception('searching')
    if s != None:
        sql = 'DELETE FROM phonebook WHERE ' + s
        cursor.execute(sql)
        conn.commit()
        print("Запись удалена.\n")


def findcontacts():
    s = key_pair_reception('searching')
    if s != None:
        sql = 'SELECT surname, name, phone_number FROM phonebook WHERE ' + s + ' ORDER BY surname'
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)


# Основная программа
print('\nПривет брат, это наша телефонная книга')
conn = sqlite3.connect('my.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook (
                id integer PRIMARY KEY,
                name text NOT NULL,
                surname text,
                phone_number text)''')
m = -1
while m != 0:
    print_menu()
    m = int(input('Выбираем: '))
    if m == 1:
        addcontact()
        continue
    elif m == 2:
        displaybook()
        continue
    elif m == 3:
        editcontacts()
        continue
    elif m == 4:
        deletecontacts()
        continue
    elif m == 5:
        findcontacts()
        continue
    elif m == 0:
        print('Программа завершена.\n')
        conn.close()
        sys.exit(0)
    else:
        print('Пожалуйста, следуйте инструкции')
