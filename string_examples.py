s1 = "spam\n"
print(len(s1))
print(s1)
s2 = 'spam\n'
print(len(s2))
print(s2)

print("foo" in "cat food")
print()

ts = "Taylor Swift"

x = ts.upper()
print(x)

print(ts.count('t'))
print(ts.lower().count('t'))

print(ts.startswith('Taylor'))
print(ts.startswith('Tom'))

print(ts.find("ay"))
print(ts.find("ya"))
print(ts.find("Tay"))

line = "foo:bar:blah:baz"
fields = line.split(':')
print(fields)

line = "Blowing in the Wind"
print(line.split())

raw_line = "Twas brilling and the slithy toves\n"
line = raw_line.rstrip()

x = "abc...,"
x = x.rstrip(',.')
print("x is", x)


raw_y = "$100,100.34"
y = raw_y.lstrip('$')
print("y is", y)

s = "     Why is the sky blue?     "
s = s.strip()
print("|" + s + "|")
























