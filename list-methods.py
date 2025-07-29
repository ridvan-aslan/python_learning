numbers = [1, 2, 3, 4, 5, 6]
letters = ['a', 'b', 'c', 'd', 'e']

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)

numbers[4] = 10

numbers.append(7)
numbers.insert(2, 8)
numbers.insert(len(numbers), 9)

# numbers.pop()
# numbers.pop(2)
# numbers.pop(-1)
numbers.remove(10)

numbers.sort()
numbers.reverse()
letters.sort()
letters.reverse()

print(numbers.count(2))
print(letters.count('a'))

numbers.clear()
letters.clear()

print(numbers)
print(letters)