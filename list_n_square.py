end=int(input("Enter upto first Square Number Want To Print : "))
list=[]
for i in range(1,end):
        s=i*i
        list.append(s)
print("List of first N prime number are " ,list)