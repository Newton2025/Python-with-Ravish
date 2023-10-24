table=int(input("Enter Table want to Print : "))
print("Table of %d is"%table)
for i in range(1,11):
    print("%d * %d = %d " %(table,i,table*i))