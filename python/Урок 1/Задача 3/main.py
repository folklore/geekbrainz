x = int(input('Введите абсциссу (но не ноль): '))
y = int(input('Введите ординату (но не ноль): '))

if x == 0:
    print('Абсцисса равна нулю')
elif y == 0:
    print('Ордината равна нулю')
elif x > 0 and y > 0:
    print('I координатный угол')
elif x < 0 and y > 0:
    print('II координатный угол')
elif x < 0 and y < 0:
    print('III координатный угол')
elif x > 0 and y < 0:
    print('IV координатный угол')
