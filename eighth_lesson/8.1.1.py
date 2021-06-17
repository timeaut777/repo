def puzir(a):
    for i in range(len(a)-1):
        for k in range(len(a)-1):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]
    print('Сортировка пузырьком выполнена успешно')

a = [int(i) for i in input().split()]
puzir(a)
print(a)

def vibor(a):
    for i in range(len(a) - 1):
        for k in range(i+1, len(a)):
            if a[k] < a[i]:
                a[k], a[i] = a[i], a[k]
    print('Сортировка выбором выполнена успешно')

a = [int(i) for i in input().split()]
vibor(a)
print(a)