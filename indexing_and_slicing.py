fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits[0] = }")
print(f"{fruits[18] = }")
print(f"{fruits[21] = }")
print(f"{fruits[len(fruits) - 1] = }")
print(f"{fruits[-1] = }")
print(f"{fruits[-2] = }")

pos = fruits.index('banana') # error if value not found
print(f"{pos = }")
print(f"{fruits[pos] = }")

print(f"{fruits = }")


# s = "red blue red red blue blue blue"
# print(f"{s.find('blue') = }")
# print(f"{s.rfind('blue') = }")

print(f"{fruits[0:4] = }")
print(f"{fruits[4:8] = }")

#  start:stop  :stop  start:  start:stop:step
print(f"{fruits[6:] = }")
print(f"{fruits[:4] = }")

artist = "Taylor Swift"
print(f"{artist[:6] = }")
print(f"{artist[2:6] = }")
print(f"{artist[7:] = }")

# slice valid for: list tuple str bytes

values = [[10, 20, 30],
        [40, 50, 60],
        [70, 80, 90],
        "wombat",
]

print(f"{type(values) = }")
print(f"{len(values) = }")
print(f"{values[0] = }")
print(f"{values[0][2] = }")
print(f"{values[3] = }")
print(f"{values[3][3] = }")
print('-' * 60)

print(f"{fruits = }")

for fruit in fruits:
    print(fruit)

# for VAR ,... in ITERABLE:
#      ...
print()

for letter in artist:
    print(letter)
print()

for fruit in fruits[0:10]:  # {
    print(fruit)
# }












