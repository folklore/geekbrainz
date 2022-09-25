finish = int(input('Введите число: '))

start = 1
results = [start]

while start < finish:
    start += 1
    results.append(start * results[-1])

print('{} -> {}'.format(finish, results))

start = 1
results = [start]

def multy(start, finish, results):
    if start <= finish:
        results.append(start * results[-1])

        if start != finish:
            multy(start + 1, finish, results)

multy(start + 1, finish, results)

print('{} -> {}'.format(finish, results))
