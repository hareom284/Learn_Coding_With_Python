fname = input("Enter file name: ")
try :
    fh = open(fname)
except:
    print(fname," files does not exit .Enter valid file names")
    quit()
for line in fh :
    line =line.rstrip()
    line.lower()
    f = open(fname, "w")
    f.write(line)