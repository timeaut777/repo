print(
    '\n'.join(
        map(lambda w1: ''.join(
            map(lambda char: chr(int(char)), w1)),
            filter(lambda x: len(x) == 6,
                   map(lambda x: x.split(), input().split(';'))))))