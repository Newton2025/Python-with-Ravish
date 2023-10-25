s_odd=0
s_even=0
element=int(input("How many Elements You Want to Enter in List : "))
odd=[]
even=[]
for i in range(element):
    n=int(input())
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)
odd.sort()
print("all odd Numbers are ",odd)
for o in odd:
    s_odd+=o
print("Sum of all odd number is " ,s_odd)
even.sort()
print("all even Numbers are ",even)
for e in even:
    s_even+=e
print("Sum of all even number is " ,s_even)