n = 0
f = []
d = []

while n != 'Stop':
    n = input()

    if 'Добавить новую фамилию' in n:
        n = n.replace('Добавить новую фамилию ', '')
        if n in f:
            print('Фамилия уже есть в списке')
        else:
            f.append(n)
            d.append(1)
        print(f, d)

    if 'Удалить по фамилии' in n:
        n = n.replace('Удалить по фамилии ', '')
        if n in f:
            index = f.index(n)
            if d[index] == 0:
                print('Фамилия уже была удалена')
            else:
                d[index] = 0
                print(f, d)
        else:
            print('В списке нет такой фамилии')

    if 'Удалить по индексу' in n:
        n = n.replace('Удалить по индексу ', '')
        n = int(n)
        if n > len(f)-1:
            print('В списке нет такого индекса')
        else:
            if d[n] == 0:
                print('Фамилия уже была удалена')
            else:
                d[n] = 0
                print(f, d)