num=int(input("Enter a number"))
new_num=num+1
i=2
while i<new_num:
    for k in range(i,new_num):
        if new_num%k==0:
            new_num+=1
print("Next prime Number is " , new_num)