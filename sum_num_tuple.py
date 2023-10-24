a=0
m=1
t=eval(input("Enter Number Separting by , : "))
for e in t:
    a=a+e
    m=m*e
print("Addition of Numbers {} ===>> {}".format(t,a))
print("Multiplication of Numbers {} ===>> {}".format(t,m))