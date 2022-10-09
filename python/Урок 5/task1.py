from random import randint

kit = ['а', 'б', 'в']
unnecessary = 'абв'

size = int(input('Enter number of words: '))

print('in')
print('Number of words:', size)

words = []
while size > 1:
    word = f'{kit[randint(0, 1)]}{kit[randint(1, 1)]}{kit[randint(1, 2)]}'
    words.append(word)
    size -= 1
joined_words = ' '.join(words)

print('out')
print(joined_words)

splited_words = joined_words.split()
filtered_words = list(filter(lambda word: word != unnecessary, splited_words))

print(' '.join(filtered_words))

# Enter number of words: 15
# in
# Number of words: 15
# out
# ббв абб ббв ббв ббб абв абв абб абб ббб ббв абв ббб ббб
# ббв абб ббв ббв ббб абб абб ббб ббв ббб ббб
