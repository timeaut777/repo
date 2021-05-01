ch = int(input())
c = []
for i in range(ch):
    a = input().split()
    b = [int(j) for j in input().split()]
    a.extend(b)
    c.append(a)

for k in range(len(c)-1):
    for l in range(len(c)-1):
        if c[l][1] > c[l+1][1]:
            c[l], c[l+1] = c[l+1], c[l]


print(c)