from common import gen_list

decimal_number = int(input('Введите десятичное число: '))
print('in')
print(decimal_number)

binary_numbers = []

while decimal_number > 0:
    remainder = decimal_number % 2
    decimal_number //= 2
    binary_numbers.insert(0, remainder)

print('out')
print(*binary_numbers, sep = '')
