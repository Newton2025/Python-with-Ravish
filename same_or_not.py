count=0
t1=eval(input("Enter Element of 1st tuple : "))
t2=eval(input("Enter Element of 2nd tuple : "))
for e in t1:
    for n in t2:
       if e==n:
        count+=1
if len(t1)==len(t2)==count:
    print("Elements Are Same")
else:
    print("Elements Are Not Same")