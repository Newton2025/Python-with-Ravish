def sum_all_element_in_list():
    element=int(input("How many Elements You Want to Enter in List : "))
    total=0
    list=[]
    while element>0:
     n=int(input())
     list.append(n)
     element-=1
    for i in list:
      total+=i
    print("Sum of all Numbers present in list is ",total)
def area_of_triangle():
    b=int(input("Enter The Breath Of a Triangle : "))
    h=int(input("Enter The Height Of a Triangle : "))
    area=b*h/2
    print("Area of Triangle : ",area)
def area_of_Circle():
    r=float(input("Enter The Radius Of Circle : "))
    area=3.1415326*(r**2)
    print("Area of Circle : ",area)

print(" =============== MENU =================== ")
n=int(input("1 : Sum of all Elements in List \n2 : Find Area of Triangle \n3 : Find Area of Circle  \n ============= END OF MENU ============= \n Enter Your Choice : "))
if n==1:
   sum_all_element_in_list()
elif n==2:
    area_of_triangle()
elif n==3:
    area_of_Circle()