import random

def get_second_digit(value):
    res = []
    exist = []
    for i in range(1,value):
        for j in range(1,value):
            if i == j:
                continue
            cur = [i,j]
            if value % (i+j) == 0 and cur not in exist:
                res.append(i)
                res.append(j)
                exist.append(cur)
                exist.append(cur.reverse())

    return int("".join(map (str, res)))

first_digit = random.choice(range(3,21))

second_digit = get_second_digit(first_digit)

print(f'{first_digit} {second_digit}')