count=0
s=input("Enter a String : ")
l=len(s)
for i in s:
    if i in " ":
       l-=1
print("Words in String ===> {} ===> {}".format(s,l))