fruits = ['pomegranate', 'banana', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'banana', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'banana', 'grape', 'date' ]

f0 = []
for f in fruits:
    value = f.upper()
    f0.append(value)
print(f"{f0 = }\n")

#    [value for var in iterable]
f1 = [f.upper() for f in fruits]  # list comprehension
print(f"{f1 = }\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"{f2 = }\n")

f3 = [f for f in fruits if f.startswith('a')]
print(f"{f3 = }\n")

banana_pos = [i for i, f in enumerate(fruits) if f == 'banana']
print(f"{banana_pos = }\n")

p_pos = [(i, f) for i, f in enumerate(fruits) if f.startswith('p') or f.startswith('a')]
print(f"{p_pos = }\n")

f_gen = (f.upper() for f in fruits)
print(f"{f_gen = }")
for fruit in f_gen:
    print(fruit)
print()

