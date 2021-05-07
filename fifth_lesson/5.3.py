ch = int(input())
a = []
b = []
for i in range(ch):
    x = input()
    y = int(input())
    if x in a:
        pass
    else:
        a.append(x)
        a.append(y)

for i in range(len(a)//2):
    b.append(a[i*2:i*2+2])

for k in range(len(b)-1):
    for l in range(len(b)-1):
        if b[l][1] > b[l+1][1]:
            b[l], b[l+1] = b[l+1], b[l]
print(b)