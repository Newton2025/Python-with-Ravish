count=0
s=input("Enter a String : ")
c=input("Enter a character whose Occurence You want to see in String : ")
for i in s:
    if i in c:
        count+=1
print("""Occurence of '{}' in "{}" ===> {}""".format(c,s,count))