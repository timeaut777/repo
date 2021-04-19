beg = 9
kor = 6
gel = 3
az = 1

for i in range(25):
    for j in range(25):
        for k in range(25):
            for l in range(25):
                s = beg * i + kor * j + gel * k + az * l
                if s == 121:
                    print('Бегемот :', i)
                    print('Коровьев :', j)
                    print('Гелла :', k)
                    print('Азазелло :', l)
                    print('---')