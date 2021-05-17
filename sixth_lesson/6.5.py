razm = 3
pole = [['*' for i in range(razm)] for k in range(razm)]
zapolneno = 1
rez = 0
pobeda = 0
flag = False
d = 0

while not (zapolneno > razm**2 or pobeda == 1):

    if zapolneno % 2 != 0:
        a = input().split()
        x = int(a[0])-1
        y = int(a[1])-1
        pole[x][y] = 'X'
        zapolneno += 1
    else:
        for i in range(len(pole)):
            for k in range(len(pole)):
                if pole[i][k] == '*':
                    pole[i][k] = '0'
                    flag = True
                    zapolneno += 1
                    break
            if flag:
                break
    flag = False
    d += 1

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

    elif zapolneno == 10:
        rez = 'Ничья'
        pobeda = 1

    if d % 2 == 0 or pobeda == 1:
        for i in pole:
            for k in i:
                print(k, end=' ')
            print()

print()
print(rez)