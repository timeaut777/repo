p = int(input())
vid = list()
kol = list()
maxIndex = 0
max = 0
c = 3

for k in range(p):
    a = input("Введите вид цветов: ")
    b = input("Введите количество цветов данного вида: ")
    vid.append(a)
    kol.append(int(b))

while c != 0:
    for i in range(len(kol)):
        if kol[i] > max:
           max = kol[i]
           maxIndex = i
    print(vid[maxIndex])
    del kol[maxIndex]
    del vid[maxIndex]
    max = 0
    c -= 1