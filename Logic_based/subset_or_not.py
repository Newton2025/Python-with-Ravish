n1=int(input("How many Element want to insert in First 1st Set : "))
s1=set()
s2=set()
for i in range(1,n1+1):
    e1=int(input("Enter %d element ===> "%i))
    s1.add(e1)
n2=int(input("How many Element want to insert in First 2nd Set : "))
for k in range(1,n2+1):
    e2=int(input("Enter %d element ===> "%k))
    s2.add(e2)
if s1.issubset(s2):
    print(" ==== S1 is Subset of S2 ====")
elif s2.issubset(s1):
    print(" ==== S2 is Subset of S1 ====")
else:
    print("'Neither s1 is subset of s2' 'nor s2 is subset of s1'")
