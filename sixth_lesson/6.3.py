a =[]
s1 = input().split()
s2 = input().split()
s3 = input().split()
a.append(s1)
a.append(s2)
a.append(s3)

for i in a:
    for k in i:
        print(k, end=' ')
    print()

if a[0][0] and a[0][1] and a[0][2] == 'X':
    print('Крестики')

if a[1][0] and a[1][1] and a[1][2] == 'X':
    print('Крестики')

if a[2][0] and a[2][1] and a[2][2] == 'X':
    print('Крестики')

if a[0][0] and a[1][0] and a[2][0] == 'X':
    print('Крестики')

if a[0][1] and a[1][1] and a[2][1] == 'X':
    print('Крестики')

if a[0][2] and a[1][2] and a[2][2] == 'X':
    print('Крестики')

if a[0][0] and a[1][1] and a[2][2] == 'X':
    print('Крестики')

if a[0][2] and a[1][1] and a[2][0] == 'X':
    print('Крестики')