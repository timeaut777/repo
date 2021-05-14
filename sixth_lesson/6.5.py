razm = 3
pole = [['*' for i in range(razm)] for k in range(razm)]
zapolneno = 0
rez = 0
pobeda = 0

while not (zapolneno > 9 or pobeda == 1):
    a = input().split()
    x = int(a[0])-1
    y = int(a[1])-1
    zapolneno += 1
    pole[x][y] = 'X'

    for i in pole:
        for k in i:
            if k != 'X' or k != '0' :
                k = '0'

    for i in pole:
        for k in i:
            print(k, end=' ')
        print()

    if pole[0][0] == 'X' and pole[0][1] == 'X' and pole[0][2] == 'X':
        rez = 'Победа крестиков'
        pobeda = 1
    elif pole[1][0] == 'X' and pole[1][1] == 'X' and pole[1][2] == 'X':
        rez = 'Победа крестиков'
        pobeda = 1
    elif pole[2][0] == 'X' and pole[2][1] == 'X' and pole[2][2] == 'X':
        rez = 'Победа крестиков'
        pobeda = 1
    elif pole[0][0] == 'X' and pole[1][0] == 'X' and pole[2][0] == 'X':
        rez = 'Победа крестиков'
        pobeda = 1
    elif pole[0][1] == 'X' and pole[1][1] == 'X' and pole[2][1] == 'X':
        rez = 'Победа крестиков'
        pobeda = 1
    elif pole[0][2] == 'X' and pole[1][2] == 'X' and pole[2][2] == 'X':
        rez = 'Победа крестиков'
        pobeda = 1
    elif pole[0][0] == 'X' and pole[1][1] == 'X' and pole[2][2] == 'X':
        rez = 'Победа крестиков'
        pobeda = 1
    elif pole[0][2] == 'X' and pole[1][1] == 'X' and pole[2][0] == 'X':
        rez = 'Победа крестиков'
        pobeda = 1

    elif pole[0][0] == '0' and pole[0][1] == '0' and pole[0][2] == '0':
        rez = 'Победа ноликов'
        pobeda = 1
    elif pole[1][0] == '0' and pole[1][1] == '0' and pole[1][2] == '0':
        rez = 'Победа ноликов'
        pobeda = 1
    elif pole[2][0] == '0' and pole[2][1] == '0' and pole[2][2] == '0':
        rez = 'Победа ноликов'
        pobeda = 1
    elif pole[0][0] == '0' and pole[1][0] == '0' and pole[2][0] == '0':
        rez = 'Победа ноликов'
        pobeda = 1
    elif pole[0][1] == '0' and pole[1][1] == '0' and pole[2][1] == '0':
        rez = 'Победа ноликов'
        pobeda = 1
    elif pole[0][2] == '0' and pole[1][2] == '0' and pole[2][2] == '0':
        rez = 'Победа ноликов'
        pobeda = 1
    elif pole[0][0] == '0' and pole[1][1] == '0' and pole[2][2] == '0':
        rez = 'Победа ноликов'
        pobeda = 1
    elif pole[0][2] == '0' and pole[1][1] == '0' and pole[2][0] == '0':
        rez = 'Победа ноликов'
        pobeda = 1

    elif zapolneno == 9:
        rez = 'Ничья'
        pobeda = 1

print()

for i in pole:
    for k in i:
        print(k, end=' ')
    print()
print()

print(rez)