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

if a[0][0] == 'X' and a[0][1] == 'X' and a[0][2] == 'X':
    print('Крестики')
elif a[1][0] == 'X' and a[1][1] == 'X' and a[1][2] == 'X':
    print('Крестики')
elif a[2][0] == 'X' and a[2][1] == 'X' and a[2][2] == 'X':
    print('Крестики')
elif a[0][0] == 'X' and a[1][0] == 'X' and a[2][0] == 'X':
    print('Крестики')
elif a[0][1] == 'X' and a[1][1] == 'X' and a[2][1] == 'X':
    print('Крестики')
elif a[0][2] == 'X' and a[1][2] == 'X' and a[2][2] == 'X':
    print('Крестики')
elif a[0][0] == 'X' and a[1][1] == 'X' and a[2][2] == 'X':
    print('Крестики')
elif a[0][2] == 'X' and a[1][1] == 'X' and a[2][0] == 'X':
    print('Крестики')

elif a[0][0] == '0' and a[0][1] == '0' and a[0][2] == '0':
    print('Нолики')
elif a[1][0] == '0' and a[1][1] == '0' and a[1][2] == '0':
    print('Нолики')
elif a[2][0] == '0' and a[2][1] == '0' and a[2][2] == '0':
    print('Нолики')
elif a[0][0] == '0' and a[1][0] == '0' and a[2][0] == '0':
    print('Нолики')
elif a[0][1] == '0' and a[1][1] == '0' and a[2][1] == '0':
    print('Нолики')
elif a[0][2] == '0' and a[1][2] == '0' and a[2][2] == '0':
    print('Нолики')
elif a[0][0] == '0' and a[1][1] == '0' and a[2][2] == '0':
    print('Нолики')
elif a[0][2] == '0' and a[1][1] == '0' and a[2][0] == '0':
    print('Нолики')

else:
    print('Никто не победил')