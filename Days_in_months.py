month=int(input("Enter The Month in Numeric Value to See it Number of Days : "))
if month in [1,3,5,7,8,10,12]:
    print("%d has 31 Days "%month)
elif month in [4,6,9,11]:
    print("%d has 30 Days "%month)
elif month in [2]:
    print("%d has 28 Days "%month)
else:
    print("Enter a Valid Month Number ")