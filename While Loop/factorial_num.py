fact=1
num=int(input("Enter a Number To Check it Factorial : "))
k=num
while num>1:
    fact*=num
    num-=1
print("Factorial of %d! ===>> %d " %(k,fact))