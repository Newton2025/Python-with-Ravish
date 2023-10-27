d={}
n=int(input("How many iteam dict what to create : "))
for i in range(1,n+1):
    print("Enter %d key" %i)
    e=input()
    print("Enter value with respect to key ",e)
    d[e]=input()
print(d)