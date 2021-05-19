a = input().split()
k = ''
b = ''
c = []

for i in a:
    k += i
    k = k.lower()
    b = k[::-1]
    if b != k or len(i) == 1:
        c.append(i)
        k = ''
        b = ''
    else:
        k = ''
        b = ''

d = ' '.join(c)
print(d)



