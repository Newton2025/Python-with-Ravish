def leap_year_or_not(year):
    if year%4==0:
        print("{} is Leap Year".format(year))
    else:
        print("{} is Not a Leap Year".format(year))
def days_year(year):
    if year%4==0:
        print("{} ===>> 366 Days".format(year))
    else:
        print("{} ===>> 365 Days".format(year))
def days_months(month):
    if month=='january' or month==1:
        print("{} ===>> 31 Days ".format(month))
    elif month=='february' or month==2:
        print("{} ===>> 28 Days ".format(month))
    elif month=='March' or month==3:
        print("{} ===>> 31 Days ".format(month))
    elif month=='April' or month==4:
        print("{} ===>> 30 Days ".format(month))
    elif month=='May' or month==5:
        print("{} ===>> 31 Days ".format(month))
    elif month=='june' or month==6:
        print("{} ===>> 30 Days ".format(month))
    elif month=='july' or month==7:
        print("{} ===>> 31 Days ".format(month))
    elif month=='August' or month==8:
        print("{} ===>> 31 Days ".format(month))
    elif month=='September' or month==9:
        print("{} ===>> 30 Days ".format(month))
    elif month=='October' or month==10:
        print("{} ===>> 31 Days ".format(month))
    elif month=='November' or month==11:
        print("{} ===>> 30 Days ".format(month))
    elif month=='December' or month==12:
        print("{} ===>> 31 Days ".format(month))
def weeks_month(month):
    print("{} ===>> 4.345 Weeks".format(month))
def days_to_month(days):
    if days<28 or days<31:
        print("1 Month")
    else:
        month=(int(days/30))
        extra_days=(int(days%30))
        print("{} ===>> {} Month and {} Days".format(days,month,extra_days))


while True:
    n=int(input("======== MENU ========= \n1: Enter 1 To Check Leap Year or Not \n2: Enter 2 To Check Number of Days in Year \n3: Enter 3 To Check Days in Month \n4: Enter 4 To Check Weeks in a Month \n5: Enter 5 To Convert Days into Month \n6: Enter 0 to Exit \n ========= MENU END ========= \nEnter What You want to see : "))
    if n==1:
        y=leap_year_or_not(int(input("Enter a Year : ")))
    if n==2:
        d=days_year(int(input("Enter a Year : ")))
    if n==3:
        m=days_months(eval(input("Enter a month : ")))
    if n==4:
        w=weeks_month(eval(input("Enter a Month : ")))
    if n==5:
        d=days_to_month(int((input("Enter Number of Days To Convert in Month : "))))
    if n==0:
        exit(0)
    k=int(input("Enter 9 To Continue : "))
    if k==9:
        continue
