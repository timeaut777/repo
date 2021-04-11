x = 100

while x!= 0:
    print('ввежите 0 для выхода')
    print('введите 1 поздороваться')
    print('введите 2 чтобы сумму')
    print('введите 3 имя 10 раз')
    x = int(input())

    if x == 1:
        print('Привет')
    elif x == 2:
        a = int(input('введите число'))
        b = int(input('введите число'))
        print(a + b)
    elif x == 3:
        name = input('имя')
        for i in range(10):
            print(name)

