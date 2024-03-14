
states = (
    'Virginia',
    'North Carolina',
    'Washington',
    'New York',
    'Florida',
    'Ohio',
)

with open("states.txt", "w") as states_out: # "w" opens for writing, "a" for append
    for state in states:
        states_out.write(state + "\n")  # write() does not automatically add newline


target = 'x'
output_file = f"{target}_words.txt"
with open('DATA/words.txt') as words_in:
    with open(output_file, "w") as words_out:
        for line in words_in:
            if line.startswith(target):
                words_out.write(line)   # \n already on input line




