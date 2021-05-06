f = input().split()

for i in range(len(f)):
    if i - 1 < 0 and i + 1 >= len(f):
        print('Предшественник:', 'нет')
        print('Текущая мумь:', f[i])
        print('Следующая мумь:', 'нет')
    if i-1 < 0 and i+1 < len(f):
        print('Предшественник:', 'нет')
        print('Текущая мумь:', f[i])
        print('Следующая мумь:', f[i+1])
    if i-1 >= 0 and i+1 < len(f):
        print('Предшественник:', f[i - 1])
        print('Текущая мумь:', f[i])
        print('Следующая мумь:', f[i+1])
    if i+1 > len(f)-1 and i-1 >= 0:
        print('Предшественник:', f[i - 1])
        print('Текущая мумь:', f[i])
        print('Следующая мумь:', 'нет')
    print('----')
