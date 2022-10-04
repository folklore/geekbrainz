from common import gen_list

numbers_count = int(input('Введите количество произвольных чисел в списке: '))
print('in')
print(numbers_count)

lst = gen_list(numbers_count, fract_part = True)
print('out')
print(lst)

min_fract = 1
max_fract = 0

for el in lst:
    fract = round(el % 1, 2)

    if fract < min_fract:
        min_fract = fract
    if fract > max_fract:
        max_fract = fract

diff = round(max_fract - min_fract, 2)
print("Min: {}, Max: {}. Difference: {}".format(min_fract, max_fract, diff))
