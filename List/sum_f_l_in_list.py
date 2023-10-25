element=int(input("How many Elements You Want to Enter in List : "))
list=[]
for k in range(element):
    n=int(input())
    list.append(n)
list.sort()
d=list[0]+list[n-1]
print("The Sum of Largest And the Smallest Number Present in list is " , d)