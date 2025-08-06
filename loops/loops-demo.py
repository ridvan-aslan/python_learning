import random

number = random.randint(1, 100)
print("Guess the number between 1 and 100.")
print(number)

rights = int(input("Enter number of attempts: "))
score = 100
score_range = score / rights

for _ in range(rights):
    your_number = int(input("Enter a number: "))
    
    if your_number == number:
        print("Congratulations! Your Score is:", round(score))
        break
    else:
        score -= score_range

        if your_number < number:
            print("Up")
        else:
            print("Down")
else:
    print("Your attempts are finished :(")