cheeses = []  # empty list
colors = list()  # empty list

cities = ['Portland', 'Pittsburgh', 'Peoria']
print(f"{len(cities) = }")
print(f"{cities = }")


print(f"cities: {cities}\n")

cities.append('Miami')
cities.append(101)
cities.append(['spam', 'ham']) 
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)
print(f"cities: {cities}\n")

# LIST.insert(pos, OBJ)  LIST.append(OBJ)   LIST.extend(ITERABLE)


del cities[3]
print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")

more_stuff = ['foo', 'bar', 'blah']
cities.append(more_stuff)
print(f"{cities = }")
cities.extend(more_stuff)
print(f"{cities = }")

print(f"{cities[7] = }")
print(f"{cities[7][1] = }")

colors = 'red', 'purple', 'crimson'

cities.append(colors)
cities.extend(colors)
print(f"{cities = }")
print(f"{cities[11][1] = }")








