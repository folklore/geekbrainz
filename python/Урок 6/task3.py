names = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]

print('in')
print(', '.join(names))
names.sort()

result = {}

for name in names:
    letter = name[0]

    if letter in result.keys():
        result[letter].append(name)
    else:
        result[letter] = [name]

print('out')
print(result)
