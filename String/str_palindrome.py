s=input("Enter a String : ")

print(s.upper())

r=s[::-1]
if s==r:
    print("Your String ===> '{}' after reverse ===> {}".format(s,r))
    print("Hence, Given String is palindrome")
else:
    print("Your String ===> '{}' after reverse ===> {}".format(s,r))
    print("Hence, Given String is not a palindrome")