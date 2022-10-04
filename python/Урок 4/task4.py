# Я не понял задание, какое-то оно слишком хардкорное, 
#   мне следует просто потренироваться писать в файл?..

from common import gen_list

numbers_count = int(input('Введите количество произвольных чисел в списке: '))
print('in')
print(numbers_count)

lst = gen_list(numbers_count)

for el in lst:
    with open('task4.txt', 'a') as file:
        file.write("{}\n".format(el))
