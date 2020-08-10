def computepay(h,r):
    if h>40 :
       return 40 * r + (h-40)*r*1.5

hrs = input("Enter Hours:")
rate = input("Enter rate")
try :
    hrs = float(hrs)
    rate = float(rate)
except :
     print("Please Enter Valid Value")
     quit()
p = computepay(hrs,rate)
print("Pay",p)