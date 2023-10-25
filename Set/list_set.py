n=int(input('Enter How many Elmemnt want to Insert in List : '))
l=[]
for i in range(n):
    e=int(input())
    l.append(e)
s=set(l)
c=len(s)
print("Number of Distinct Elements in List ===>> ",c)