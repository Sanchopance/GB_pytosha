# Мимикрия
transformation = lambda x: x
values = [1, 23, 42, "asdfg"]
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')


# Самая далёкая планета

def find_farthest_orbit(arr):
    return [i for i in arr if i[0] * i[1] == max([i[0] * i[1] for i in arr if i[0] != i[1]])][0]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))


# Винни-пух
def param(s):
    a = s.split()
    count = 0
    cl = []
    check = 'ауоыэяюёие'
    for i in a:
        for j in i:
            for g in check:
                if g in j:
                    count += 1
        if count > 0:
            cl.append(count)
        count = 0
    y = cl[0]
    b = list(filter(lambda x: x == y, cl))
    if len(cl) == len(b):
        return True
    else:
        return False


phrase = str(input('Введите фразу: '))
if param(phrase):
    print("Парам пам-пам")
else:
    print("Пам парам")


# Все равны, как на подбор с ними дядька Черномор
def same_by(characteristic, objects):
    a = []
    for i in objects:
        if characteristic(i) == 0:
            a.append(True)
        else:
            a.append(False)
    y = a[0]
    b = list(filter(lambda x: x == y, a))
    if len(a) == len(b):
        return True
    else:
        return False


values = [0, 2, 4, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


# Безимянная задачка
def print_operation_table(operation, num_rows, num_columns):
    if operation == '*':
        for i in range(1, num_rows + 1):
            for j in range(i, i * num_columns + 1, i):
                print(j, end='\t')
            print()
    if operation == '+':
        for i in range(1, num_rows + 1):
            for j in range(i, i + num_columns + 1, i):
                print(j, end='\t')
            print()
    if operation == '**':
        for i in range(1, num_rows + 1):
            for j in range(i, i ** num_columns + 1, i):
                print(j, end='\t')
            print()


numrows = int(input('Введите количество строк: '))
operations = str(input('Введите операцию (*, +, **): '))
numcolumns = int(input('Введите количество колонок: '))
print_operation_table(operations, numrows, numcolumns)
