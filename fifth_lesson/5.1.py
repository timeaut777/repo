ch = int(input())
f = list()
a = []
for i in range(ch):
    c = input()
    f.append(c)

for j in f:
    if j not in a:
        a.append(j)

print(a)