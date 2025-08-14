import random

# result = dir(random)
# result = help(random)
result = random.random() # Generates a random float between 0.0 and 1.0
result = random.random() * 100 # Generates a random float between 0.0 and 100.0
result = random.uniform(1, 10) # Generates a random float between 1.0 and 10.0
result = random.randint(1, 10) # Generates a random integer between 1 and 10

greeting = "Hello, World!"

names = ["Alice", "Bob", "Charlie", "David"]

result = names[random.randint(0, len(names) - 1)]
# result = random.choice(names) # Randomly selects an element from the list
result = random.choice(greeting)
result = random.sample(names, 2) # Randomly selects 2 unique elements from the list

my_list = list(range(1, 11)) # Creates a list of integers from 1 to 10
random.shuffle(my_list) # Shuffles the list in place
result = my_list
result = random.sample(my_list, 2)

print(result)