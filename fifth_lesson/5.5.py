command = 0
index = int
a = []
b = []
c = []
while command != 'Stop':
    command = input()

    if 'Добавить новую фамилию' in command:
        command = command.split()
        command = command[len(command)-1]
        if command not in a:
            a.append(command)
            b.append(1)

    if 'Удалить по индексу' in command:
        command = command.split()
        command = command[len(command) - 1]
        index = int(command)
        if index < len(b):
            b[index] = 0
        else:
            print('В списке нет такого индекса')

    if 'Удалить по фамилии' in command:
        command = command.split()
        command = command[len(command) - 1]
        if command in a:
            for i in range(len(a)):
                if command == a[i]:
                    b[i] = 0
        else:
            print('В списке нет такой фамилии')

print(a, b, sep='\n')

for j in range(len(b)):
    if b[j] == 1:
       c.append(a[j])
print(c)






