from common import gen_list

numbers_count = int(input('Введите количество произвольных чисел в списке: '))
print('in')
print(numbers_count)

lst = gen_list(numbers_count)
print('out')
print(lst)

# Я искренне не понимаю, как питонисты раскуривают такие записи ...
nw_lst = [x for i, x in enumerate(lst) if i == 0 or x > lst[i - 1]]
print(nw_lst)
