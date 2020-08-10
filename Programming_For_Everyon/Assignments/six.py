fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    line = line[20:]
    line = float(line)
    total = total+line
   

print("Average spam confidence:",total/count)