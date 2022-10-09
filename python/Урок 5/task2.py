from random import randint
import string

####

basic_letters = string.ascii_letters
letters = []

unique_letters_counter = randint(5, 25)
while unique_letters_counter > 1:
    letter = basic_letters[randint(0, len(basic_letters) - 1)]
    letters.append(letter * randint(0, 10))
    unique_letters_counter -= 1

input_file_name = 'text_words.txt' # input('Enter the name of the file with the text: ')

with open(input_file_name, 'w') as file:
    for letter in letters:
        file.write(letter)

with open(input_file_name, 'r') as file:
    text = file.readline()

print('input file\'s content:')
print(text)

###

def rle_coder(text):
    n = 0
    rle_content = []
    text_size = len(text)

    while n < text_size:
        letter = text[n]
        count = 1

        condy = True
        while condy and n < (text_size - 1):
            n += 1
            next_letter = text[n]

            if letter == next_letter:
                count += 1
            else:
                condy = False

        rle_content.append(count)
        rle_content.append(letter)

        if condy:
            n += 1

    return rle_content

output_file_name = 'text_code_words.txt' # input('Enter the file name to record: ')

with open(output_file_name, 'w') as file:
    for content in rle_coder(text):
        file.write(str(content))

with open(output_file_name, 'r') as file:
    rle_content = file.readline()

print('output file\'s content:')
print(rle_content)

###

def rle_decoder(rle_content):
    text = ''
    counters = []
    letters = []
    now = 'number' # Из-за повторений символов более 9 раз городить пришлось ... ((

    for symbol in rle_content:
        if symbol.isdigit():
            if now == 'number':
                counters.append(symbol)
            else:
                counters[len(counters) - 1] += symbol
            now = 'letter'
        else:
            letters.append(symbol)
            now = 'number'

    for index, letter in enumerate(letters):
        text += int(counters[index]) * letter

    return text

print('result:')
print(rle_decoder(rle_content))

# input file's content:
# XXXXXXXXXXKKKKKKKKKKKLLLCCCCCdddVVVVVVVVVVrr
# output file's content:
# 10X11K3L5C3d10V2r
# result:
# XXXXXXXXXXKKKKKKKKKKKLLLCCCCCdddVVVVVVVVVVrr
