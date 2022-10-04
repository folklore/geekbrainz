from common import gen_list

numbers_count = int(input('Введите количество произвольных чисел в списке: '))
print('in')
print(numbers_count)

print('out')
new_lst = []

if(numbers_count < 0):
    print('Negative value of the number of numbers!')
else:
    lst = gen_list(numbers_count)

    for el in lst:
        if el not in new_lst:
            new_lst.append(el)

    print(lst)

print(new_lst)
