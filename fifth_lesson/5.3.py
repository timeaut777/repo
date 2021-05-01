ch = int(input())
c = []
s = []
for i in range(ch):
    a = input().split()
    b = input().split()
    a.extend(b)
    print(a)