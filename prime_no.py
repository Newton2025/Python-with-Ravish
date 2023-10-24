num=int(input("Enter a Number : "))
count=0
for i in range (2,num):
  if num%i==0:
    count+=1
if count==1:
   print("%d is not Prime Number " %num)
else:
    print("%d is Prime Number " %num)