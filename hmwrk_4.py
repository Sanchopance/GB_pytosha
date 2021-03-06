# 1. Вычислить число Пи c заданной точностью
import random
from decimal import *

getcontext().prec = 1 + int(input('Введите точность числа Пи: '))
pi = Decimal(0)
i = Decimal(0)

while i < 1000:
    pi = pi + 1 / (16 ** i) * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
    i = i + 1

print('Число Пи =', pi)

# 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых делителей числа N.
# (1 - составное число)

nat = int(input('Введите число N: '))


def natnumbers(n):
    r = [1, n]
    i = 2
    while i * i <= n:
        if n % i == 0:
            r = r + [i]
            k = n // i
            if k != i:
                r = r + [k]
        i += 1
    return r


print('Список простых делителей числа', nat, '->', natnumbers(nat))

# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности
numbers = [0, 0, 1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 8, 9, 9]
unical_numbers = list(set(numbers))
print('Последовательность чисел ->', numbers)
print('Неповторяющиеся элементы исходной последовательности ->', unical_numbers)

# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и вывести на экран.
# Не мое, подсмотрел, времени совсем нет, прошу понять и простить)

def polynomial(k):
    s = ''
    r = 0
    for i in range(k, 0, -1):
        r = random.randint(0, 101)
        if r == 0:
            s += ''
        elif r == 1:
            s += str(f'x^{i} + ')
        elif i != 1:
            s += str(f'{r}x^{i} + ')
        else:
            s += str(f'{r}x ')
    r = random.randint(0, 101)
    if r != 0:
        s += str(f'+ {r} = 0')
    else:
        s += str(f'= 0')
    return s


k = int(input("Введите натуральную степень: "))
print(polynomial(k))