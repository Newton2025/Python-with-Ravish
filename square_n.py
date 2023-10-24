s=int(input("Enter start from : "))
u=int(input("Enter End at : "))
print("Square of Numbers from %d to %d is "%(s,u))
for i in range(s,u+1):
    print(i,i**2,sep=' ==> ')