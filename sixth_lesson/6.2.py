razm = 3
pole = [['*' for i in range(razm)] for k in range(razm)]
command = input()

while command != 'Stop':
    a = input().split()
    x = int(a[0])-1
    y = int(a[1])-1

    if x > razm-1 or y > razm-1:
        print('Такой координаты не существует!')
    elif pole[x][y] == '*' and command == 'Крестик':
        pole[x][y] = 'X'
    elif pole[x][y] == '*' and command == 'Нолик':
        pole[x][y] = '0'
    elif pole[x][y] == 'X' or pole[x][y] == '0':
        print('На этом поле уже стоит символ!')

    command = input()

for i in pole:
    for k in i:
        print(k, end=' ')
    print()