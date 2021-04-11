a, b, c, d = int(input()), int(input()), int(input()), int(input())
x = d*b/c
y = d*c/b

if a == 1:
    print(d, 'Руб', 'это', x, '$')
else:
    print(d, '$', 'это', y, 'Руб')
