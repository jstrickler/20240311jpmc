
fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'lemon', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'lemon', 'blueberry', 'lychee', 'grape', 'date' ]

pos = fruits.index('lemon')
print(f"{pos = }")

all_lemon_pos = []
for i, fruit in enumerate(fruits):
    if fruit ==  'lemon':
        all_lemon_pos.append(i)
print(f"{all_lemon_pos = }")

print(f"{list(enumerate(fruits)) = }")

e = enumerate(fruits)
print(e)

for i, fruit in e:
    print(i, fruit)
print('-' * 60)

colors = ['red', 'purple', 'pink']

for c in reversed(colors):
    print(c)
print()

r = reversed(colors)
print(f"{r = }")
for color in r:
    print(color)
print()

numbers = [10, 20, 30]
print(f"{colors = }")
print(f"{numbers = }")

x = zip(colors, numbers)
print(f"{list(x) = }")
print(f"{list(x) = }")
print()

for i in range(5):
    print(i)
print()

#  range(stop)   range(start, stop)  range(start, stop, step)

for i in range(1, 6):
    print(i)
print()

MAX_TRIES = 3
# for i in range(MAX_TRIES):
#     x = make_connection()
#     # sleep 1 second
#     if x:
#         break


