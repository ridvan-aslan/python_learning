number = int(input("Enter your number: "))

if number == 1:
    print(f"{number} is not a prime number.")
else:
    isPrime = True

    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break

    if isPrime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
