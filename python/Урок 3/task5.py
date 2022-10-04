number = int(input('Задайте число: '))
print('in')
print(number)
number = abs(number)

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

i = 1
fibs = [0]

while i < number:
    res = fib(i)
    fibs.append(res)

    if i % 2 == 0:
        fibs.insert(0, -res)
    else:
        fibs.insert(0, res)

    i += 1

print(fibs)
