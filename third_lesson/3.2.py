a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a >= b:
    if a >= c:
        if a >= d:
            print('1')
if b >= a:
    if b >=c:
        if b >= d:
            print('2')
if c >= a:
    if c >= b:
        if c >= d:
            print('3')
if d >= a:
    if d >= b:
        if d >= c:
            print('4')

