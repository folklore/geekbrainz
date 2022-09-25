position_1 = int(input('Position one: '))
position_2 = int(input('Position two: '))
number = int(input('Number of elements: '))

if number < 0:
    number *= -1

collection = []
current = -number

while current <= number:
    collection.append(current)
    current += 1

collection_size = len(collection)

verify = position_1 > 0 and \
         position_2 > 0 and \
         position_1 < (collection_size + 1) and \
         position_2 < (collection_size + 1)

if verify:
    result = collection[position_1 - 1] * collection[position_2 - 1]

    print(f'-> {collection}')
    print(f'-> {result}')
