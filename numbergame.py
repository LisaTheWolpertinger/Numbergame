import random

randomnumber = random.randint(1,100)

print("Welcome to the great number game! Let's see, if you can guess the number I am thinking about.")
tip = int(input("Tip a number between 1 and 100: "))

while tip != randomnumber:
    if tip > randomnumber:
        print("The Number you are looking for must be smaller. Try again! Your last tip:",tip)
        tip = int(input("Your next tip: "))
    elif tip < randomnumber:
        print("The Number you are looking for must be larger. Try again! Your last tip:", tip)
        tip = int(input("Your next tip: "))

print("Yeah, That's right! It was",randomnumber, "! Congrats!" )