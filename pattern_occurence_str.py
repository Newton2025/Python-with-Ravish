count=0
s=input("Enter a String : ")
p=input("Enter a pattern want to find in string : ")
l=s.split(" ")
for i in l:
    if i==p:
        count+=1
print("Pattern found ===> {} Times ".format(count))