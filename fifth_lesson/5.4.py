n = int(input())
f = input().split()
d = [0]*(len(f))

for i in range(len(f)):
    if i-n >= 0:
        d[i-n] = f[i]
    else:
        d[len(f)+i-n] = f[i]

print(d)