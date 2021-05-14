razm = 3
pole = [['*' for i in range(razm)] for k in range(razm)]
s = 0
v = 0
r = 0
while not (s > 9 or r == 1):
    a = input().split()
    x = int(a[0])-1
    y = int(a[1])-1
    s += 1

    if s % 2 == 0:
        pole[x][y] = '0'
    else:
        pole[x][y] = 'X'

    for i in pole:
        for k in i:
            print(k, end=' ')
        print()

    if pole[0][0] == 'X' and pole[0][1] == 'X' and pole[0][2] == 'X':
        v = 'Победа крестиков'
        r = 1
    elif pole[1][0] == 'X' and pole[1][1] == 'X' and pole[1][2] == 'X':
        v = 'Победа крестиков'
        r = 1
    elif pole[2][0] == 'X' and pole[2][1] == 'X' and pole[2][2] == 'X':
        v = 'Победа крестиков'
        r = 1
    elif pole[0][0] == 'X' and pole[1][0] == 'X' and pole[2][0] == 'X':
        v = 'Победа крестиков'
        r = 1
    elif pole[0][1] == 'X' and pole[1][1] == 'X' and pole[2][1] == 'X':
        v = 'Победа крестиков'
        r = 1
    elif pole[0][2] == 'X' and pole[1][2] == 'X' and pole[2][2] == 'X':
        v = 'Победа крестиков'
        r = 1
    elif pole[0][0] == 'X' and pole[1][1] == 'X' and pole[2][2] == 'X':
        v = 'Победа крестиков'
        r = 1
    elif pole[0][2] == 'X' and pole[1][1] == 'X' and pole[2][0] == 'X':
        v = 'Победа крестиков'
        r = 1

    elif pole[0][0] == '0' and pole[0][1] == '0' and pole[0][2] == '0':
        v = 'Победа ноликов'
        r = 1
    elif pole[1][0] == '0' and pole[1][1] == '0' and pole[1][2] == '0':
        v = 'Победа ноликов'
        r = 1
    elif pole[2][0] == '0' and pole[2][1] == '0' and pole[2][2] == '0':
        v = 'Победа ноликов'
        r = 1
    elif pole[0][0] == '0' and pole[1][0] == '0' and pole[2][0] == '0':
        v = 'Победа ноликов'
        r = 1
    elif pole[0][1] == '0' and pole[1][1] == '0' and pole[2][1] == '0':
        v = 'Победа ноликов'
        r = 1
    elif pole[0][2] == '0' and pole[1][2] == '0' and pole[2][2] == '0':
        v = 'Победа ноликов'
        r = 1
    elif pole[0][0] == '0' and pole[1][1] == '0' and pole[2][2] == '0':
        v = 'Победа ноликов'
        r = 1
    elif pole[0][2] == '0' and pole[1][1] == '0' and pole[2][0] == '0':
        v = 'Победа ноликов'
        r = 1

    else:
        v = 'Ничья'

print()

for i in pole:
    for k in i:
        print(k, end=' ')
    print()
print()

print(v)