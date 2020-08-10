largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try :
       num = int(num)
       if (largest==None) :
          largest = num
       if  (smallest==None) :
           smallest =num
       if largest < num :
           largest = num
       if smallest >num :
        smallest = num
    except :
        print("Invalid Input")
        if num == 'done':
           break
print("Maximum is",largest)
print("Minimum is",smallest)