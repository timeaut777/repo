ch = int(input())
f = list()
for i in range(ch):
    c = input()
    f.append(c)
k = 0
for i in range(len(f)-1):
    for j in range(len(f)-1):
        if f[j] > f[j+1]:
            f[j], f[j+1] = f[j+1], f[j]
            k += 1
print(f, k, sep='\n')