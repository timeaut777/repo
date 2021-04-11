a = int(input())
b = input()
b = int(b)

a1 = a//100 + (a//10)%10 + a%10
b1 = (b//100 + (b//10)%10 + b%10)

if a1 == b1 and 999 > b >= 100:
    print(a, b + 1, sep='')
if a == 999 and b == 999:
    print(a, '000', sep='')

if a1 == b1 and 10 <=b < 100:
    print(a, 0, b + 1, sep='')
if a1 == b1 and b<10:
    print(a, 0, 0, b + 1, sep='')


if a1 != b1 and b >= 100:
    print(a, b, sep='')
if a1 != b1 and 10 <=b < 100:
    print(a, 0, b, sep='')
if a1 != b1 and b<10:
    print(a, 0, 0, b, sep='')






