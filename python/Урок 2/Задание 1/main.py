original_number = float(input('Введите вещественное число: '))

if original_number == round(original_number):
    original_number = int(original_number)

number = original_number

if number < 0:
    number *= -1
while number != round(number):
    number *= 10

summa = 0

while number != 0:
    summa += number % 10
    number = number // 10

print('Число: {}; сумма цифр: {}'.format(original_number, int(summa)))
