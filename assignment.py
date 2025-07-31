# x = 5
# y = 10
# z = 25

x, y, z = 5, 10, 25

# x, y = y, x

x += 5    # x = x + 5
x -= 5    # x = x - 5
x *= 5    # x = x * 5
x /= 5    # x = x / 5
x %= 5    # x = x % 5
x //= 5   # x = x // 5

y //= 5   # y = y // 5
y **= 5   # y = y ** 5



values = 1, 2, 3, 4, 5

print(values)
print(type(values))

x, y, *z = values

print(x, y, z)
print(x, y, z[1])
