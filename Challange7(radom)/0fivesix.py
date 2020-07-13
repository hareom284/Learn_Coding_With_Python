import random

num = random.randint(1,10) #get radom number between 1 to 10
print(num)

number =int(input("Guess a Number"))

while(number!=num) :
    number = int(input("Try again"))
print("Well done")