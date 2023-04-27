#теорія
print("lkdfwek", 2123, 9.0)

def black_hole(*args):
    print(type(args))
    print(args)
    for argument in args:
        print(argument)

black_hole(234, "Earth", "rusnya", "time", 6776)

def black_hole_named(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for argument in kwargs:
        print(argument)
black_hole_named(name="Gleb", planet="Earth", number = 5)