sum=0
i=1
n=int(input("Enter value of n : "))
while i<=n:
    if i%2!=0:
      sum=sum+i
    i+=1
print("Sum of Natural Number is ",sum)