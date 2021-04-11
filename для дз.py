vid = int(input())
max1 = 0
max2 = 0
max3 = 0
for k in range(vid):
    cv = input()
    kol = int(input())
    if kol > max1:
        max2 = max1
        max1 = kol
    elif kol > max2:
        max3 = max2
        max2 = kol
    elif kol > max3:
        max3 = kol

print(max1, max2, max3)


