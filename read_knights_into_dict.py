from pprint import pprint

knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_info[name] = title, color, quest, comment

pprint(knight_info)
print()
print(f"{knight_info['Galahad'] = }")
print(f"{knight_info['Galahad'][1] = }")
print()


