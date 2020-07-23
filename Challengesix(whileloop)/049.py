compnum = 50
count = 1
num = int(input("Enter a Number"))
while num != compnum:
   if num > 50 :
     print("Your guess is too high")
   else :
     print("Your guess is too low")
   count = count + 1
   num = int(input("Enter another guess"))
   
   
print(f'Well done,you took {count} attempts')
   