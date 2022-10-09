from random import randint

# А для чего в примере boolean после числа?
# in
# 10 True

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

number = int(input('Введите N (больше 0): '))

if number < 0:
    print('N должно быть больше 0! Bye.')
    exit

print('in')
print(number)

dictionaries = [nouns, adverbs, adjectives]
phrases = []

while number > 0:
    phrase = [dictionary[randint(0, len(dictionary)-1)] for dictionary in dictionaries]
    phrases.append(' '.join(phrase))
    number -= 1

print('out')
print(phrases)
