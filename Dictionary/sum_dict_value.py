d={}
bill=0
n=int(input("Enter Number of Products Buyed : "))
for i in range(1,n+1):
    e=input("Enter Product Name  : ")
    d[e]=int(input("Enter price of Product {}  : ".format(e)))
print(" ========== Bill of Your buy is Given below ==========")
for k in d:
    bill=bill+d[k]
    print(k,d[k],sep='   ===>>  ')
print("Total Amount ===>> ",bill)
print(" ========== Hope You Like This Digital Billing System ==========")