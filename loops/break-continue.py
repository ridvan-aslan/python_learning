name = "Rıdvan Aslan"

# for letter in name:
#     if letter == "ı":
#         continue
#     print(letter)

x = 0

# while x < 5:
#     if(x == 3):
#         break
#     print(x)
#     x += 1

total = 0
i = 0

while i <= 100 :
    i += 1
    if i % 2 == 0:
        continue
    total += i

print(f"The sum of all odd numbers from 1 to 100 is {total}")