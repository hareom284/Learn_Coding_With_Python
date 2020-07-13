import random
colours = random.choice(["red","green","blue","cyan","pink"])
choice = input("Enter a color name")
choice.lower()
while(colours!=choice):
   print("You are probably feel",colours,"right now!")
   choice = input("Enter colour again")
   choice.lower()
print("Well done!")