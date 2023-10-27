d={}
n=int(input("Enter size of a dict want to create : "))
for i in range(1,n+1):
    e=input("Enter %d key : "%i)
    d[e]=input("Enter value with respect to {} key : ".format(e))
temp=d[e]
for k in d:
    if k>=temp:
        print(k,d[k],sep='===>>')