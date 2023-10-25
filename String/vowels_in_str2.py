count=0
Vowel="aeiouAEIOU"
s=input("Enter a String : ")
for i in s:
    if i in Vowel:
        count=count+1
print("Number of Vowels in string ===> ",count)