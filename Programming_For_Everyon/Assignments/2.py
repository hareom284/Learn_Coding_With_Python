count =0
while True :
    line = input(">")
    if line[0]=="#":
        continue
    if line=="done":
        break
    print(line)
    count= count+1
    print(count)
print('Done!')