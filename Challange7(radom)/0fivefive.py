import random
computer = random.randint(1, 7)
print(computer)
userchoice = int(input("Choice a Number between 1 to 7"))
while(computer!=userchoice) :
    userchoice = int(input("Try second guess"))

    if(userchoice>computer):
       print("Your guess too high")
    elif (userchoice < computer):
        print("Your guess too low")
print("Well done")
       
