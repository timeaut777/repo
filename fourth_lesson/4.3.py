do = input()
c = 0

while do != 'Пришли полицейские':
    price1 = int(input())
    price2 = int(input())
    do = input()
    if price1 > c:
        c = price1
    if price2 > price1:
        c = price2

print(c)