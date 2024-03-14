def hello_jpmc():
    print("Hello, JPMC world")

hello_jpmc()
hello_jpmc()

def hello(whom: str="world"):  # :str is a type hint -- ignored by interpreter
    print(f"Hello, {whom}")

hello("world")
hello("kitty")
hello("New York")
hello()

hello(123)
hello([1,2,3])

def find_word(word_to_find, *files_to_search):
    for file in files_to_search:
        with open(file) as file_in:
            for line in file_in:
                if word_to_find in line:
                    print(line.rstrip())


find_word('bird', 'DATA/alice.txt', 'DATA/parrot.txt')

def triple(thing):
    return thing * 3

x = triple(10)
print(f"{x = }")

print(f"{triple('jump') = }")
print(f"{triple([True]) = }")

def spam():
    print("spam spam spam")

x = spam()
print(f"{x = }")


