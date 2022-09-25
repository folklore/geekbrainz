import random

number = int(input('Длина списка: '))
print(number)

collection = []

while number >= 1:
    collection.insert(0, number)
    number -= 1
print(f'-> {collection}')

index = 0
collection_size = len(collection)

while index < collection_size:
    rand = random.randint(0, collection_size - 1)
    collection[rand], collection[index] = collection[index], collection[rand]
    index += 1
print(f'-> {collection}')

# Длина списка: 10
# 10
# -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# -> [5, 8, 2, 1, 9, 7, 4, 10, 3, 6]
