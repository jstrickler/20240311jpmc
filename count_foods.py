
file_name = 'DATA/breakfast.txt'

food_counts = {}

with open(file_name) as food_in:
    for raw_food in food_in:
        food = raw_food.rstrip()
        if food in food_counts:
            food_counts[food] += 1  # food_counts[food] = food_counts[food] + 1
        else:
            food_counts[food] = 1
        
print(food_counts)