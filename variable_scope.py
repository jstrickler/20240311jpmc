
x = 100  # global (to file)

def spam():
    x = 50  # still local!!
    m = "mothballs"  # local (to function)
    print(f"{m = }")
    print(f"{x = }")
    

spam()

# print(f"{m = }")
print(f"{x = }")
