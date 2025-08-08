# def change_name(n):
#     n = "Ada"

# name = "Rıdvan"

# change_name(name)

# print(name)

# new section

# def change(n):
#     n[0] = "İstanbul"

# cities = ["Ankara", "İzmir"]

# change(cities)

# print(cities)

# new section

# def add(*params):
#     sum = 0
#     for n in params:
#         sum +=n
#     return sum

# print(add(2, 3))
# print(add(2, 3, 5))
# print(add(2, 3, 5, 7, 10, 12))

# new section

# def display_user(**args):
#     print("User Information")
#     for key, value in args.items():
#         print(f"{key}: {value}")

# display_user(name="Rıdvan", surname="Aslan", age=22, city="Tekirdağ")

# new section

def my_func(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print("args:", args)
    print("kwargs:", kwargs)

my_func(10, 20, 30, 40, name="Rıdvan", surname="Aslan", age=22, key = "value")
