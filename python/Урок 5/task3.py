import os

cells = 9 * [None]


def print_field(cells):
    os.system('cls' if os.name == 'nt' else 'clear')

    print('-----------------')
    i = 0

    while i <= 2:
        j = 0
        line = []

        while j <= 2:
            number = i * 3 + j
            if cells[number]:
                output = cells[number]
            else:
                output = number+1
            line.append(f'  {output}  ')
            j += 1

        print('|'.join(line))
        i += 1
        print('-----------------')


def to_be_continue(cells):
    return not any_win(cells) and not drawn_game(cells)


# Не придумал как сделать лучше ...
def any_win(cells):
    winner = None

    # Проверка по горизонталям
    i = 0
    while i <= 2:
        if cells[i * 3 + 0] == cells[i * 3 + 1] and cells[i * 3 + 1] == cells[i * 3 + 2]:
            winner = cells[i * 3 + 0]
            break
        i += 1

    # Проверка по вертикалям
    j = 0
    while j <= 2:
        if cells[j + 0] == cells[j + 3] and cells[j + 3] == cells[j + 6]:
            winner = cells[j + 0]
            break
        j += 1

    # Диагональ вниз
    if cells[0] == cells[4] and cells[4] == cells[8]:
        winner = cells[0]

    # Диагональ вверх
    if cells[2] == cells[4] and cells[4] == cells[6]:
        winner = cells[2]

    if winner != None:
        print_field(cells)
        print(f'{winner} - Win!')
        return True
    return False


def drawn_game(cells):
    if not None in cells:
        print_field(cells)
        print('Drown game!')
        return True
    return False


run = True
step = 'x'
flash = None

while run:
    print_field(cells)

    if flash != None:
        print(flash)
        flash = None

    print('Enter a number from 1 to 9.')
    position = input(f'Select a position "{step}"? ')

    if not position.isdigit() or int(position) < 1 or int(position) > 9:
        flash = f'"{position}" - incorrect input! 🚫'
    else:
        if cells[int(position) - 1] != None:
            flash = f'"Cell {position}" is already occupied!'
        else:
            cells[int(position) - 1] = step
            run = to_be_continue(cells)
            step = 'o' if step == 'x' else 'x'
