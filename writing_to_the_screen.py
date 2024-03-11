
name = "Taylor Swift"
x = 45
value = 98.390239
print(name)
print()  # print blank line (only '\n')
print(name, x, value)

print(name, x, value, sep="//")

print(name, end=" ")
# conditionally print something
print(value)

print(x, ":", name)
# print(x + ": " + name)

print(f"{x}: {name}")   # f-string AKA formatted string

print("{}: {}".format(x, name))   # older

print("%d: %s" % (x, name))  # ancient

print(f"2 + 2 is {2 + 2}")

print(value)
print(f"{value:.1f}")

print(x)
print(f"{x:4d}")
print(f"{x:04d}")

print("{:04d}".format(x))







