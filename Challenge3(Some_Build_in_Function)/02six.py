latin = input("Enter pig Latin")
firstword =latin[0]
length = len(latin)
if firstword == 'a' or firstword == 'e' or firstword == 'i' or firstword == 'u' :
    newword = latin+"way"
    print(newword)

else:
    consolt = firstword+"ay"
    print(latin[1:length],consolt)