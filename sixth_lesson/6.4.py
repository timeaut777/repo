razm = 3
pole = [['*' for i in range(razm)] for k in range(razm)]
s = 0

while not 'Победа' or 'Все поля заполнены':
    a = input().split()
    x = int(a[0])-1
    y = int(a[1])-1
    pole[x][y] = 'X'
    s += 1

    if s == 9:
        print('Все поля заполнены')

    b = input().split()
    w = int(b[0]) - 1
    z = int(b[1]) - 1
    pole[w][z] = '0'
    s += 1
    if s == 9:
        print('Все поля заполнены')

for i in pole:
    for k in i:
        print(k, end=' ')
    print()