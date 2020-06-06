total = 0
for i in range(2,7) :
    num = int(input("Enter a Number"))
    ans = input("Do you want this number included?(Y/N)")
    if ans == "y" :
        total = total + num
print(total)

