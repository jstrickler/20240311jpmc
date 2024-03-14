x = list()   # instance = class()
# list x = new list();
x.append('wombat')
x.append('pastafazool')
print(f"{x.count('wombat') = }")
print(f"{type(x) = }")
print()

y = list()
y.append('red')
y.append('blue')
y.insert(1, "orange")

class Dog:
    def bark(self):   #   self:Python::this:Java
        print("Woof! woof!")

d1 = Dog()  # create object/instance
d1.bark()  # call instance method from object/instance




