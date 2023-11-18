class Employee:
    def __init__(self):
        self.employees=[]
        self.employee_list=[]
    def get_employee_data(self):
        n=int(input("Enter Number of Employee : "))
        for i in range(n):
            name=input("Enter Employee Name : ")
            self.employee_list.append(name)
            Salary=int(input("Enter Employee Salary: "))
            employee={'Name':name,'Salary':Salary}
            self.employees.append(employee)
    def employees_data(self):
       print(self.employees)
    def list_employee(self):
        print(self.employee_list)
          
emp=Employee()

emp.get_employee_data()
print("Employee Name with Salary:")
emp.employees_data()
print("Employee Name:")
emp.list_employee()

