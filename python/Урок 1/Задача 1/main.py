day_number = int(input('Введите цифру, обозначающую день недели: '))

weekend_numbers = [6, 7]

if day_number in weekend_numbers:
    print('Выходной день')
elif day_number < 1 or day_number > 7:
    print('Нет такого дня')
else:
    print('Будний день')
