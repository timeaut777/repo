n = int(input())
f = input().split()

for i in range(n):
    f = f[1:] + f[:1]

print(f)