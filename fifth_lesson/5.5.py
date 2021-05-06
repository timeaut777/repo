command = 0
a = []
b = []
while command != 'Stop':
    command = input()

    if command == 'Добавить новую фамилию':
        f = input()
        if f in a:
            pass
        else:
            a.append(f)
            b.append(1)
    print(a, b)

    if command == 'Удалить по индексу':
        index = int(input())
        if index < len(b):
            b[index] = 0
        else:
            print('В списке нет такого индекса')
    print(a, b)

    if command == 'Удалить по фамилии':
        f = input()
        if f in a:
            for i in range(len(a)-1):
                if f == a[i]:
                    b[i] = 0

        else:
            print('В списке нет такой фамилии')
    print(a, b)






