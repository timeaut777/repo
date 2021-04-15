kol_m = int(input())
s_m = 0
s_z = 0
for i in range(kol_m):
    number_m = int(input())
    s_m += number_m
for i in range(kol_m + 1):
    number_z = int(input())
    s_z += number_z
print(s_z - s_m)
