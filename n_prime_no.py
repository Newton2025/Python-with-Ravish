num=int(input("Enter last Number : "))
count=0
for i in range(1,num,2):
    if num%i!=0 and num!=1:
        print(i)