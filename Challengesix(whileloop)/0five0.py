num = int(input("Guess a Number between 10 to 20"))
while num < 10 or num > 20:
    if num < 10 :
        print("Too low")
    else :
        print("Too High")
    num = int(input("Try again : "))
print("Your right")
         
         