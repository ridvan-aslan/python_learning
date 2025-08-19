my_list = [1, 2, 3, 4, 5]

iterator = iter(my_list)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))

# for i in my_list:
#     print(i)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

class MyNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.end:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
# for x in MyNumbers(1, 10):
#     print(x)

my_class = MyNumbers(1, 10)
my_iter = iter(my_class)

# print(next(my_iter))
# print(next(my_iter))

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break