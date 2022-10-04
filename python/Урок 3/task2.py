from common import gen_list

numbers_count = int(input('Введите количество произвольных чисел в списке: '))
print('in')
print(numbers_count)

lst = gen_list(numbers_count)
print('out')
print(lst)

res = []

while len(lst) > 1:
    res.append(lst.pop(0) * lst.pop(-1))
if len(lst):
    res.append(lst.pop())

print(res)
