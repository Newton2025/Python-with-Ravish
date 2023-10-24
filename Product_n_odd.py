p=1
n=int(input("Enter upto product of odd Number Want : "))
for i in range(1,n+1):
    if i%2!=0:
        p=i*p
print("Product of N Odd Number ====>> ",p)