import random
score = 0
for i in range(1,7) :
    num1 = random.randint(1,40)
    num2 = random.randint(1,40)
    correct= num1 + num2
    print (num1,"+",num2,"=")
    answer = int(input("Enter Your Answer"))
    if(correct == answer):
        score = score + 1
print("Your score is",score,"out of 7")