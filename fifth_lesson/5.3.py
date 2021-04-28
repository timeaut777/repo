ch = int(input())

for i in range(ch):
    f = input().split()
    l = [int(i) for i in input().split()]
    l.sort()
    f.extend(l)
print (f)