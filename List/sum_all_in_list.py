element=int(input("How many Elements You Want to Enter in List : "))
total=0
list=[]
while element>0:
    n=int(input())
    list.append(n)
    element-=1
for i in list:
    total+=i
print("Sum of all Numbers present in list is ",total)