full_names = ["Иван Сергеев", "Инна Серова", "Петр Алексеев",
         "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
         "Борис Аркадьев", "Антон Серов", "Павел Анисимов"]

print('in')
print(', '.join(full_names))

def sorter(full_name):
    name, surname = full_name.split()
    return([surname[0], name[0]])
full_names.sort(key = sorter)

result = {}

for full_name in full_names:
    name, surname = full_name.split()

    surname_letter = surname[0]
    name_letter = name[0]

    if surname_letter in result.keys():
        if name_letter in result[surname_letter].keys():
            result[surname_letter][name_letter].append(full_name)
        else:
            result[surname_letter][name_letter] = [full_name]
    else:
        result[surname_letter] = {name_letter: [full_name]}

print('out')
print(result)
