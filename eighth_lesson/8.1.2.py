def sorting(a, typ):

    if typ == 'puz':
        for i in range(len(a) - 1):
            for k in range(len(a)-1):
                if a[k] > a[k+1]:
                    a[k], a[k+1] = a[k+1], a[k]
        print('Сортировка пузырьком выполнена успешно')

    elif typ == 'vib':
        for i in range(len(a) - 1):
            for k in range(i + 1, len(a)):
                if a[k] < a[i]:
                    a[k], a[i] = a[i], a[k]
        print('Сортировка выбором выполнена успешно')

a = [int(i) for i in input().split()]
typ = input()
sorting(a, typ)
print(a)



