element=int(input("How many Elements You Want to Enter in List : "))
list=[]
for k in range(element):
    n=int(input())
    list.append(n)
g=list[0]
for i in list:
    if i>g:
        g=i
print("greatest Number in List is " ,g)