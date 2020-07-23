# Turples
fruit_tuple = ("apple","banana","straberry","orange")
# print(fruit_tuple.index("banana"))
#to get index from tuple
# print(fruit_tuple[2])
# namelist = ["Zaw","Hare","Sam","Win"]
# # del namelist[3]
# print(len(namelist))
# namelist.append(input("Add another name"))
# print(namelist)
# namelist.sort()
# print(sorted(namelist))
# print(namelist[0])
####dictionay 
# colour = {1:"red",2:"green",3:"blue"}
# colour[2] ="white"
# print(colour)
x = [123,32,733,432,"hello"]
num = int(input('Enter a Number'))
if num in x :
    print("Number is in the list")
else:
    print("Number is not int the list")
x.insert(2,420)
x.remove("hello")
print(x)