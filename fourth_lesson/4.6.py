x = int(input())

print('*    *')
print('******')
print('* ** *')
print('*    *')
print('******')
print('  **  ')
print('******')
print('*    *')
print('*    *')
print('*    *')
print('******')

i = 0
for i in range(x):
    for j in range(i):
        print(' ', end='')
    print('  **  ')
    for j in range(i):
        print(' ', end='')
    print('  **  ')
    i += 1
