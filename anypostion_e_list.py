element=int(input("How many Elements You Want to Enter in List : "))
print(" And its Position for Each elements to place it")
total=0
list=[]
for i in range(element):
     print("Enter Postion")
     p=int(input())
     print("Enter Element")
     n=int(input())
     list.insert(p,n)
print("list are ",list)


