n = input()
f = input().split()
m = -1
index = -1
for i in range(len(f)):
    
    if i + n <= len(f):
        i = i + n
    else:
        i = (i + n) % len(f)
print(f)