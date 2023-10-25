end=int(input("Enter upto first Prime Number Want To Print : "))
list=[]
for i in range(1,end):
    for k in range(1,i):
        count=i%k
        if count==2:
            list.append(k)
        else:
            pass
print("List of first N prime number are " ,list)