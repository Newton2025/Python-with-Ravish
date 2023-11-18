class Employee:
    def employee_data(self):
        try:
            self.empid=int(input("Enter empid : "))
            self.name=input("Enter Employee Name : ")
            self.salary=int(input("Enter Employee Salary : "))
        except ValueError:
            print("oops! Looking like you have not Entered empid and Salary in Interger")
    def display_data(self):
        print("empid : ",self.empid)
        print("Name : ",self.name)
        print("Salary : ",self.salary)
emp1=Employee()

emp1.employee_data()
emp1.display_data()