
# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
spisok = [2, 3, 5, 9, 3]
summa = 0
for el in range(len(spisok)):
    if el % 2 != 0:
        summa += spisok[el]
print('Список элементов ->', spisok)
print('Сумма элементов списка, стоящих на нечётной позиции =', summa)

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
numbers = [2, 3, 4, 5, 6]


def multnumbers(nums):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0] * numbers[-1])
        del numbers[0]
        del numbers[-1]
    if len(numbers) == 1: results.append(numbers[0] ** 2)
    return results


print('Наш список ->', numbers)
print('Произведение пар чисел списка ->', multnumbers(numbers))

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

numbers = [1.1, 1.2, 3.1, 5.1, 10.01]
def diff(nums):
    nums = [round(a - int(a), 2) for a in (numbers)]
    return max(nums) - min(nums)

print (numbers)
print(diff(numbers))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
num = int(input('Введите число: '))

def dec_to_bin(num):
    bin_num = ''
    while num != 0:
        bin_num += str(num % 2)
        num = num // 2
    return bin_num[::-1]
print('Число', num, 'в двоичной системе =', dec_to_bin(num))

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input('Введите число k: '))


def negofibonacci(k):
    fibo_nums = []
    a, b = 1, 1
    for i in range(k - 1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(k):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums


fibo_nums = negofibonacci(k)
print(negofibonacci(k + 1))
