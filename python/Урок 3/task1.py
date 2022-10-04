from common import gen_list

numbers_count = int(input('Введите количество произвольных чисел в списке: '))
print('in')
print(numbers_count)

lst = gen_list(numbers_count)
print('out')
print(lst)

print(sum(lst[0::2]))
