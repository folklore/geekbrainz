number = float(input('Enter a real number: '))
print('in')
print(number)

accuracy = float(input('Enter the required accuracy \'0.0001\': '))

n = 0

while accuracy < 1:
    n += 1
    accuracy *= 10

print('out')
print(f"%.{n}f" % number)
