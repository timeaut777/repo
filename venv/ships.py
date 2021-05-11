razm = 4
first = [[0 for i in range(razm)] for k in range(razm)]
second = [[0 for i in range(razm)] for k in range(razm)]
ships = 2
f_frags = 0
s_frags = 0

for i in range(ships):
    a = input('Игрок 1, введите координаты корабля').split()
    x = int(a[0]) - 1
    y = int(a[1]) - 1
    first[x][y] = 1

for i in range(ships):
    a = input('Игрок 2, введите координаты корабля').split()
    x = int(a[0]) - 1
    y = int(a[1]) - 1
    second[x][y] = 1

while f_frags < ships and s_frags < ships:
    a = input('Игрок 1, введите координаты выстрела').split()
    x = int(a[0]) - 1
    y = int(a[1]) - 1
    if second[x][y] == 1:
        f_frags += 1
        second[x][y] = 2
        print('убит')
    else:
        second[x][y] = '*'
        print('промазал')

    a = input('Игрок 2, введите координаты выстрела').split()
    x = int(a[0]) - 1
    y = int(a[1]) - 1
    if first[x][y] == 1:
        s_frags += 1
        first[x][y] = 2
        print('убит')
    else:
        first[x][y] = '*'
        print('промазал')

if s_frags == ships and f_frags == ships:
    print('ничья')

elif s_frags == ships:
    print('победа 2-ого игрока')

elif f_frags == ships:
    print('победа 1-ого игрока')
else:
    print('ошибка')

for i in first:
    for k in i:
        print(k, end=' ')
    print()

print()

for i in second:
    for k in i:
        print(k, end=' ')
    print()

