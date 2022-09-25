finish = int(input('Введите число: '))
start = 1
results = []

while start <= finish:
    result = round((1 + 1 / start) ** start)
    results.append(result)
    start += 1
print('{} -> {}'.format(finish, results))

results = []
n = finish

while n >= 1:
    result = round((1 + 1 / n) ** n)
    results.insert(0, result)
    n -= 1
print('{} -> {}'.format(finish, results))
