a = input().split()
upper = 0
lower = 0
for i in a:
    for j in i:
        if j.isupper():
            upper += 1
        else:
            lower += 1
if upper > lower:
    print(a)

