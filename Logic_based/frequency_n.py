end=int(input("Enter upto first Square Number Want To Print : "))
list=[]
for i in range(1,end):
        n=int(input())
        list.append(n)
for k in list:
    c=list.count(k)
    print("Occurence of Number are %d ==> %d " %(k,c))