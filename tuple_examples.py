
person = "Bill", 'Gates', "Microsoft", "1955-10-24"

# person[0] = "Fred"   INVALID

print(f"{person = }")
print(f"{type(person) = }")

print(f"{person[0] = }")
print(f"{person[1] = }")

# alternatives to tuples:
#     namedtuple    provide named element
#     dataclass     provide class with properties and methods

first_name, last_name, product, dob = person  # unpacking the tuple
print(f"{first_name = }")
print(f"{last_name = }")

# var, var, ... = ITERABLE

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
print(f"{type(people) = }")
print(f"{people[0] = }")
print(f"{type(people[0]) = }")
print(f"{people[0][0] = }")
print(f"{people[0][0][0] = }")
print('-' * 60)

for person in people:
    first_name, last_name, product, dob = person
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, *_ in people:
    print(first_name, last_name)
print('-' * 60)


