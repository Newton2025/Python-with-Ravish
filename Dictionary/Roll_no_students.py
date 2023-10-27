d={}
n=int(input("Enter Number of students  : "))
for i in range(1,n+1):
    print("Enter Student Name for Roll No : ",i)
    s=input()
    d[i]=s
for s in d:
    print("Roll No. : {} ===>> {}".format(s,d[s]))