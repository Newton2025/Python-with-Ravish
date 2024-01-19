from prettytable import PrettyTable

class Bank:
    def __init__(self):
        # Create Account in Bank
        self.Customer_ID = None
        self.Customer_Name = None
        self.Customer_Contact_No = None
        self.Account_Number = None
        self.Customer_Detail=None

    def set_Customer_ID(self,Customer_ID):
        self.Customer_ID = Customer_ID

    def get_Customer_ID(self):
        return self.Customer_ID

    def set_Customer_Name(self,Customer_Name):
        self.Customer_Name = Customer_Name

    def get_Customer_Name(self):
        return self.Customer_Name

    def set_Customer_Contact_Number(self,Customer_Contact_Number):
        self.Customer_Contact_No = Customer_Contact_Number

    def get_Customer_Contact_Number(self):
        return self.Customer_Contact_No

    def set_Account_Number(self,Account_Number):
        self.Account_Number = Account_Number

    def get_Account_Number(self):
        return self.Account_Number

    def get_Customer_Detail(self):
        customer_detail = {}
        customer_detail["Customer ID"] = self.Customer_ID
        customer_detail["Customer Name"] = self.Customer_Name
        customer_detail["Customer Number"] = self.Customer_Contact_No
        customer_detail["Account Number"] = self.Account_Number
        return customer_detail

all_detail=[]
process=True
while process:
        userInput = int(input("1. Press 1 to Create Account\n2. Press  0  for all_detail\nEnter your choice: "))
        if userInput == 1:
            acc = Bank()
            Customer_id=int(input("Enter Customer ID : "))
            acc.set_Customer_ID(Customer_id)
            Customer_Name=input("Enter Customer Name : ")
            acc.set_Customer_Name(Customer_Name)
            Account_Number=int(input("Enter Account Number : "))
            acc.set_Account_Number(Account_Number)
            Customer_Contact_Number=int(input("Enter Customer Contact Number : "))
            acc.set_Customer_Contact_Number(Customer_Contact_Number)
            customer_detail = acc.get_Customer_Detail()
            print("Customer Id must be an integer")
            table = PrettyTable(["Attribute", "Value"])
            for key, value in customer_detail.items():
                table.add_row([key, value])
            print(table)
            all_detail.append(table)
        else:
            process = False
for i in all_detail:
 print("{}:{}".format(i))