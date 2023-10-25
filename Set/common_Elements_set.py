n_s1=int(input("How many elements you want to insert in set 1: "))
s1=set()
for i in range(n_s1):
    n1=int(input())
    s1.add(n1)
n_s2=int(input("How many elements you want to insert in set 2: "))
s2=set()
for k in range(n_s2):
    n2=int(input())
    s2.add(n2)
intersect=s1.intersection(s2)
print("Common elements in Both the Sets are : ",intersect)