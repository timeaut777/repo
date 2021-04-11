c = int(input())
k = int(input())

if k <= 5:
    print(c * k)
if 10 >= k > 5:
    print(int(c*k - c*k*25/100))
if k > 10:
    print(int(c*k - c*k*50/100))



