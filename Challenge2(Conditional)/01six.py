raining = raw_input("Is it Raining?")
raining = raining.lower()
if raining =="yes" :
  windy = raw_input("Is it Windy")
  windy = windy.lower()
  if windy =="yes" :
      print("It is too windy for an umbrella")
  else :
      print("Take an umbrella")    
else :
    print("Enjoy your day")      