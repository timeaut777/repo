vid = int(input())
s = 0
for k in range(vid):
    cv = input()
    kol = int(input())
    while vid >= 3:
        if kol > s:
            s = kol
print(s)


