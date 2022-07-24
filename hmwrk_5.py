# Конфеты
# Человеки
import random
from random import randint, choice

greeting = ('Вас приветствует игра "Забери все конфеты!" '
            'Итак, начнём!')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def play_game(n, m, players, messages):
    count = 0
    if n % 10 == 1 and 9 > n > 10:
        letter = 'а'
    elif 1 < n % 10 < 5 and 9 > n > 10:
        letter = 'ы'
    else:
        letter = ''
    while n > 0:
        print(f'{players[count % 2]}, {random.choice(messages)}')
        move = int(input())
        if move > n or move > m:
            print(f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -= 1
            else:
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!\n')
        n = n - move
        if n > 0:
            print(f'Осталось {n} конфет{letter}')
        else:
            print('Все конфеты разобраны.\n')
        count += 1
    return players[not count % 2]


print(greeting)

player1 = input('Первый игрок, введите имя\n')
player2 = input('Второй игрок, введите имя\n')
players = [player1, player2]

n = int(input('Сколько конфет будем разыгрывать?\n '))
m = int(input('Сколько максимально будем брать конфет за один ход?\n '))

winer = play_game(n, m, players, messages)
if not winer:
    print('У нас нет победителя.\n')
else:
    print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!\n')

# Человек и бот

greeting = ('******************************************************\n'
            'Вас приветствует игра "Забери все конфеты! с Ботом')

messages = [
    "Ваша очередь брать конфеты",
    "возьмите конфеты",
    "сколько конфет возьмёте?",
    "берите, не стесняйтесь",
    "Ваш ход",
]


def introduce_players():
    player1 = input("Как Вас зовут?\n")
    player2 = "Бот"
    print(f"А я тупой {player2}")
    return [player1, player2]


def get_rules(players):
    n = int(input("Сколько конфет будем разыгрывать?\n "))
    m = int(input("Сколько максимально будем брать конфет за один ход?\n "))
    first = int(input(f"{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую цифру\n"))
    if first != 1:
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    count = rules[2]
    print(count)
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = "а"
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = "ы"
    else:
        letter = ""
    while rules[0] > 0:
        if not count % 2:
            move = rules[0] % rules[1] + 1
            print(f"Я забираю {move}")
        else:
            print(f"{players[0]}, {choice(messages)}")
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(f"Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}")
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f"Попробуйте ещё раз, у Вас {attempt} попытки")
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f"Очень жаль, у Вас не осталось попыток. Game over!")
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f"Осталось {rules[0]} конфет{letter}")
        else:
            print("Все конфеты разобраны.")
        count += 1
    return players[not count % 2]


print(greeting)

players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print("У нас нет победителя.\n")
else:
    print(f"Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!\n")

# *************************************************
# Крестики нолики
print('Крестики нолики - погнали!\n')
board = list(range(1,10))

def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(board)

# RLE
print('RLE текст в файле rle.txt\n'
      'результат декода ниже, лежит в файле rle_enc.txt\n')
with open('rle.txt', 'r') as data:
    my_text = data.read()


def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


str_code = encode_rle(my_text)
print(str_code)
dev_12 = str_code

with open('rle_enc.txt', 'w') as data:
    data.write(dev_12)


# Все украдено с просторов, нужно очень много времени, увы, но сейчас его совсем нет