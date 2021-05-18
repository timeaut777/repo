# 7.2

a = input()
for i in range(len(a)):
    if i % 2 == 0 or a[i].isupper():
        print(a[i], end='')


