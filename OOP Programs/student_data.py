class student:
    def __init__(self):
        self.rollno=None
        self.name=None
        self.semester=None
        self.branch=None
    def get_user_data(self):
        try:
          self.rollno=int(input("Enter Roll No. : "))
        except ValueError:
            print("Something Went Wrong !,'Roll No Must be Integer' ")
        self.name=input("Enter Student Name : ")
        try:
          self.semester=int(input("Enter Semester : "))
        except ValueError:
            print("Something Went Wrong !,'Semester Must be in Integer' ")
        self.branch=input("Enter Branch : ")
    def display_data(self,i):
        print(f"{i} Student Data are : ")
        print("Roll No. : ",self.rollno)
        print("Name : ",self.name)
        print("Semester. : ",self.semester)
        print("Branch : ",self.branch)
#Here student1 is object of class Student()
student1=student()
#Here student2 is also object of class Student()
student2=student()

#Calling function with instance
print("Enter 1st Student Data :")
student1.get_user_data()
print("Enter 2nd Student Data :")
student2.get_user_data()

#Display Function is runing to print data
student1.display_data(1)
student2.display_data(2)