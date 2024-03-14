
sh_counts = {}

with open('DATA/passwd') as pw_in:
    for raw_line in pw_in:
        line = raw_line.rstrip()
        *_, shell = line.split(':')
        if shell in sh_counts:  # if key already in dictionary
            sh_counts[shell] += 1
        else:  # key not in dictionary
            sh_counts[shell] = 1

for shell, count in sh_counts.items():
    print(shell, count)
