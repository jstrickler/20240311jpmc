
file_path = "DATA/presidents.txt"

with open(file_path) as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip()  # remove \n
        fields = line.split(':') 
        if fields[-1] == 'Whig':
            print(fields[2], fields[1])
print('-' * 60)

target = 'x'

count = 0
with open('DATA/words.txt') as words_in:
    for line in words_in:
        if line.startswith(target):
            count += 1
            print(line.rstrip())
print(f"{count} words start with {target}")