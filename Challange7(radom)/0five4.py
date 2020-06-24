import random
computer = random.choice(["head","tail"])

userchoice = input("Enter your choice 1.Head 2.Tail")
if  (computer =="head" and userchoice =="1") or(computer=="tail" and userchoice=="2"):
    print("You Win")
else:
    print("Bad Luck")
