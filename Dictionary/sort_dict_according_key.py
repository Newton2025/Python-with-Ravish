d={}
n=int(input("Enter size of dict  : "))
for i in range(1,n+1):
    print("Enter %d Key : "%i)
    s=input()
    print("Enter value according to Key ",s)
    d[s]=input()
temp=s
for k in d:
    if k>=temp:
        print(k,d[k],sep='===>>')