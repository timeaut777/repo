vid = int(input())
max1 = 0
max2 = 0
max3 = 0
max1cv = str
max2cv = str
max3cv = str

for k in range(vid):
    cv = input()
    kol = int(input())
    if kol > max1:
        max3 = max2
        max3cv = max2cv
        max2 = max1
        max2cv = max1cv
        max1 = kol
        max1cv = cv
    elif kol > max2:
        max3 = max2
        max3cv = max2cv
        max2 = kol
        max2cv = cv
    elif kol > max3:
        max3 = kol
        max3cv = cv

print(max1cv, max2cv, max3cv, sep='\n')