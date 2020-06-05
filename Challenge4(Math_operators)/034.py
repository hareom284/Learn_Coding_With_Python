condition = int(input("1)Square \n2)Triangle "))
if condition == 1 :
    lenght = int(input("Enter the length"))
    area = lenght * lenght
    print("The area of square is ",area)

elif condition == 2:
    base1 =int(input("Enter base"))
    height = int(input("Enter Height"))    
    area =height*base1*(1/2)
    print("The area of triangle is ",area)
else:
    print("Invalid Input")    