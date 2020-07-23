# # def computepay(h,r):
# #     if h>40 :
# #        return 40 * r + (h-40)*r*1.5

# # hrs = input("Enter Hours:")
# # rate = input("Enter rate")
# # try :
# #     hrs = float(hrs)
# #     rate = float(rate)
# # except :
# #      print("Please Enter Valid Value")
# #      quit()
# # p = computepay(hrs,rate)
# # print("Pay",p)

# # while True :
# #     line = input('>')
# #     if line[0]=="#":
# #         continue
# #     if line=="done":
# #         break
# #     print(line)
# # print('Done!')


# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     try :
#        num = int(num)
#        if (largest==None) :
#           largest = num
#        if  (smallest==None) :
#            smallest =num
#        if largest < num :
#            largest = num
#        if smallest >num :
#         smallest = num
#     except :
#         print("Invalid Input")

#     if num == 'done':
#         break
# print("Maximum is",largest)
# print("Minimum is",smallest)
#Write code using find() and string slicing(see section 6.10)
#  to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.
# text = "X-DSPAM-Confidence:    0.8475"
# start = text.find('0')
# end   = text[start:29]
# end = float(end)
# print(end)
#7.1 Write a program that prompts for a file name, 
# then opens that file and reads through the file,
#  and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# fname = input("Enter file name: ")
# try :
#     fh = open(fname)
# except:
#     print(fname," files does not exit .Enter valid file names")
#     quit()
# for line in fh :
#     line =line.rstrip()
#     print(line.upper())
# Use the file name mbox-short.txt as the file name
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
