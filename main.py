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

def black_hole_named(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)
black_hole_named(name="Gleb", planet="Earth", number = 5)


def black_hole_full(var1, *args, var2 = 2, **kwargs):
    if not args: #для перевірки наявності не іменнованих аргументів
        return  0
    for argument in args:
        print(argument)
    for key, value in kwargs.items():
        print(key, value)
    print(var1)
black_hole_full(234, "Earth", "rusnya", "time", 6776,
                name="Gleb", planet="Earth", number = 5)

lst = [2,3,4]
dict = {"n":1, "b":2, "n1":3}
def fun(var_1, var_2, var_3):
    print(var_1, var_2, var_3)
fun(*lst)
def fun_dict(n, b, n1):
    print(1, 2, 3)
fun_dict(**dict)