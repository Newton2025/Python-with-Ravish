n=int(input("How may Elements Want to Enter in Set : "))
count=0
s=set()
for i in range (1,n+1):
    e=int(input("enter %d Element : "%i))
    s.add(e)
for c in s:
    count+=1
print("Elements in set are : ",count)