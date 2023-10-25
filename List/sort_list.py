element=int(input("How many Elements You Want to Enter in List : "))
list=[]
while element>0:
    n=input()
    list.append(n)
    element-=1
list.sort()
print(list)