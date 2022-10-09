import random

def gen_list(size, fract_part = False):
    lst = []
    while size > 0:
        if fract_part:
            rand = round(random.uniform(0.01, 9.99), 2)
        else:
            rand = random.randint(10, 100)

        lst.append(rand)
        size -= 1

    return lst
