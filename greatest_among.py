num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : " ))
num3=int(input("Enter Third Number : "))
if num1>num2 and num1>num3:
    print("%d is The Greatest Number "%num1)
elif num2>num3:
    print("%d is The Greatest Number "%num2)
else:
    print("%d is The Greatest Number "%num3)