sub1=float(input("Enter Geography Marks : "))
sub2=float(input("Enter Biology Marks : "))
sub3=float(input("Enter physics Marks : "))
sub4=float(input("Enter Chemistry Marks : "))
sub5=float(input("Enter Mathematics Marks : "))
marks_obtained=(sub1+sub2+sub3+sub4+sub5)/5
if marks_obtained>44 and marks_obtained<101:
    print(marks_obtained,"PASS",sep=' ==> ')
elif marks_obtained<=44:
    print(marks_obtained,"FAIL",sep=' ==> ')
else:
    print("Enter a Valid Marks")