do = input()
c = 0
a = 0

while do != 'При':
    price1 = int(input())
    price2 = int(input())
    do = input()

    if c < 100:
       if price1 > price2:
          c = price1
       else:
          c = price2

    else:
        if price1 < price2:
            c = price1
        else:
            c = price2

    c += c

print(c)