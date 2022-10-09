number = int(input('Введите N (больше 20): '))

if number < 20:
    print('N должно быть больше 20! Bye.')
    exit

result = [n for n in range(20, number) if n % 20 == 0 or n % 21 == 0]
print(result)
