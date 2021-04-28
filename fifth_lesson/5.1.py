k = int(input())

for i in range(k):
    f = [int(i) for i in input().split()]
    for j in f:
        a = []
        if j not in a:
            a.append(j)

print(a)