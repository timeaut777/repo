dlin = int(input())
a = 0
j = 0
max_j = 0

for i in range(dlin//100):
    v = int(input())
    if v > a:
        a = v
        j += 1
        if j > max_j:
            max_j = j
    elif v <= a:
        a = v
        j = 0

print(max_j * 100)
