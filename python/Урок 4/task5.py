in_file_names = ['task5.x.txt', 'task5.y.txt']
out_file_name = 'task5.z.txt'
lines = []

print('in')

for file_name in in_file_names:
    print(file_name)

    with open(file_name, 'r') as file:
        lines += file.readlines()

print('out in the file')

for line in lines:
    with open(out_file_name, 'a') as file:
        file.write(line)

with open(out_file_name, 'r') as file:
    print(*file.readlines())
