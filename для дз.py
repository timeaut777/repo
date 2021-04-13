dlin = int(input())
a = 0
j = 0
s = 0
k = 0
max = 0

for i in range(dlin//100):
    v = int(input())
    while v > a:
        a = v
        j += 1
    if v <= a:
        a = v
        s = j

    if s > j:
        max = s
    else:
        max = j

    j = 0

print(max)


