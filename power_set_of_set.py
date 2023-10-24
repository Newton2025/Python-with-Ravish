n=int(input("Enter how many Element want to Insert in set 1 : "))
s1=set()
s=set()
for i in range(n):
    e=int(input())
    s1.add(e)
for x in s1:
    s.add(x**2)
print("square of Set {} ===>> {}".format(s1,s))