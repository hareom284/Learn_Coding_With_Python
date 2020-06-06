number = int(input("How many people you need to invit"))
if number < 10 :
    for i in range(0,10):
       name=input("Enter Name")
       print(name,"has been invited")
else:
    print("Too many people")       
