k = int(input())

for i in range(k):
    f = [int(i) for i in input().split()]

a = []
for j in f:
    if j == j+1:
        a.append(j)
    else:
        a.append(j)
        a.append(j+1)

print(a)