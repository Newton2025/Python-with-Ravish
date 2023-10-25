s=int(input("Start from : "))
e=int(input("End at : "))
d=int(input("Difference between number : "))
print("Number from range %d to %d with Common Difference %d are :"%(s,e+1,d))
for i in range(s,e,d):
    print(i)