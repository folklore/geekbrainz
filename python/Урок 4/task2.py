number = int(input('Задайте натуральное число N: '))
print('in')
print(number)

def find_multipliers(n):
    multipliers = []
    i = 2

    while i <= n:
        if n % i == 0:
            multipliers.append(i)
            n = n / i
            i = 2
        else:
            i = i + 1

    return multipliers

print('out')
print(find_multipliers(number))
