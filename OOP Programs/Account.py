class Account:
    rate_of_interest = 0

    def __init__(self):
        self.balance = 50000
        self.account_number = 26382827123

    def show_balance(self):
        print("Balance: ", self.balance)

    def show_rate_of_interest(self, rate, time):
        self.rate_of_interest = (self.balance * rate * time) / 100
        print("Rate of Interest: ", self.rate_of_interest)

    def withdrawal_detail(self, withdrawal=0):
        self.balance -= withdrawal
        print(f"Balance after withdrawal {withdrawal} ==>> ", self.balance)

    def deposit_detail(self, deposit=0):
        self.balance += deposit
        print(f"Balance after deposit {deposit} ==>> ", self.balance)


acc = Account()
while True:
    user_choice = input(
        "\nTo See Balance type: show_balance\nTo see Rate of Interest type: show_interest\nTo withdraw type: withdrawal\nTo deposit type: deposit\nEnter 'exit' to close\nEnter Choice: "
    )
    if user_choice == "show_balance":
        acc.show_balance()
        continue
    if user_choice == "show_interest":
        acc.show_rate_of_interest(
            int(input("Enter rate: ")), int(input("Enter time period: "))
        )
        continue
    if user_choice == "withdrawal":
        withdrawal = int(input("Enter Amount to withdraw: "))
        acc.withdrawal_detail(withdrawal)
        continue
    if user_choice == "deposit":
        deposit = int(input("Enter Amount to deposit: "))
        acc.deposit_detail(deposit)
        continue
    if user_choice == "exit":
        exit(0)
