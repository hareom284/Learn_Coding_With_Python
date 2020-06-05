first = input("Enter Your First Name")
if len(first) < 5 :
    surname = input("Enter Your Surname")
    fullname = first + surname;
    print(fullname.strip(" "))
else :
    print("You don't need to write your surname")