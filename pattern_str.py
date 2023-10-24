s=input("Enter a String : ")
p=input("Enter a pattern want to find in string : ")
l=s.split(" ")
for i in l:
    if i==p:
      print("Patter Found")
      break
print("Patter Not Found")