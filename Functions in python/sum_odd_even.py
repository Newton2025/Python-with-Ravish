def even_sum(s,u):
    a=0
    for i in range(s,u+1):
        if i%2==0:
            a+=i
    return a
def odd_sum(s,u):
    a=0
    for i in range(s,u+1):
        if i%2!=0:
            a+=i
    return a

c=int(input("========== MENU ============ \n1 : Enter 1 For Sum of All Even Number from Given range \n2 : Enter 2 For Sum of All Odd Number from Given range \n ========= MENU END ========= \nEnter Your Choice : "))
if c==1:
    s=even_sum(int(input("Enter Sum of Even Number from which want to print : ")),(int(input("Enter upto Sum of Even Number want to print : "))))
    print("Sum of Even Number ==>> ",s)
if c==2:
    s=odd_sum(int(input("Enter Sum of odd Number from which want to print : ")),(int(input("Enter upto Sum of odd Number want to print : "))))
    print("Sum of odd Number ==>> ",s)