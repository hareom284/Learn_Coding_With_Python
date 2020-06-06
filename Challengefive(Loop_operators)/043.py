number = int(input("Enter a Number between 1 t0 100"))
direction = int(input("1)Up\n2)Down"))
if direction == 1:
    for i in range(1,number,1):
        print(i)
elif direction ==2:
    for i in range(number,1,-1):
        print(i)
else:
    print("Please Enter Valid Input")
       