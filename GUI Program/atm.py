import tkinter as tk
from tkinter import ttk

class AccountGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Account Management")

        self.acc = Account()

        self.page_var = tk.StringVar()
        self.page_var.set("HomePage")

        self.show_home_page()

    def show_home_page(self):
        self.clear_window()

        self.balance_label = ttk.Label(self.master, text="Balance:")
        self.balance_label.grid(row=0, column=0, padx=10, pady=10)

        self.balance_var = tk.StringVar()
        self.balance_var.set(f"${self.acc.balance}")
        self.balance_display = ttk.Label(self.master, textvariable=self.balance_var)
        self.balance_display.grid(row=0, column=1, padx=10, pady=10)

        self.action_label = ttk.Label(self.master, text="Select an action:")
        self.action_label.grid(row=1, column=0, padx=10, pady=10)

        self.actions = ["Show Balance", "Show Interest", "Withdrawal", "Deposit", "Exit"]
        self.action_var = tk.StringVar()
        self.action_dropdown = ttk.Combobox(self.master, textvariable=self.action_var, values=self.actions)
        self.action_dropdown.grid(row=1, column=1, padx=10, pady=10)
        self.action_dropdown.set("Show Balance")

        self.submit_button = ttk.Button(self.master, text="Submit", command=self.show_selected_page)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_selected_page(self):
        user_choice = self.action_var.get()

        if user_choice == "Show Balance":
            self.show_home_page()
        elif user_choice == "Show Interest":
            self.show_interest_page()
        elif user_choice == "Withdrawal":
            self.show_withdrawal_page()
        elif user_choice == "Deposit":
            self.show_deposit_page()
        elif user_choice == "Exit":
            exit(0)
        else:
            print("Invalid choice. Please try again.")

    def show_interest_page(self):
        self.clear_window()

        self.rate_label = ttk.Label(self.master, text="Enter rate:")
        self.rate_label.grid(row=0, column=0, padx=10, pady=10)

        self.rate_var = tk.StringVar()
        self.rate_entry = ttk.Entry(self.master, textvariable=self.rate_var)
        self.rate_entry.grid(row=0, column=1, padx=10, pady=10)

        self.time_label = ttk.Label(self.master, text="Enter time period:")
        self.time_label.grid(row=1, column=0, padx=10, pady=10)

        self.time_var = tk.StringVar()
        self.time_entry = ttk.Entry(self.master, textvariable=self.time_var)
        self.time_entry.grid(row=1, column=1, padx=10, pady=10)

        self.submit_button = ttk.Button(self.master, text="Submit", command=self.show_interest_result)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_interest_result(self):
        rate = float(self.rate_var.get())
        time = int(self.time_var.get())
        result = self.acc.show_rate_of_interest(rate, time)
        self.show_result_page(result)

    def show_withdrawal_page(self):
        self.clear_window()

        self.withdrawal_label = ttk.Label(self.master, text="Enter Amount to withdraw:")
        self.withdrawal_label.grid(row=0, column=0, padx=10, pady=10)

        self.withdrawal_var = tk.StringVar()
        self.withdrawal_entry = ttk.Entry(self.master, textvariable=self.withdrawal_var)
        self.withdrawal_entry.grid(row=0, column=1, padx=10, pady=10)

        self.submit_button = ttk.Button(self.master, text="Submit", command=self.show_withdrawal_result)
        self.submit_button.grid(row=1, column=0, columnspan=2, pady=10)

    def show_withdrawal_result(self):
        withdrawal = int(self.withdrawal_var.get())
        result = self.acc.withdrawal_detail(withdrawal)
        self.show_result_page(result)

    def show_deposit_page(self):
        self.clear_window()

        self.deposit_label = ttk.Label(self.master, text="Enter Amount to deposit:")
        self.deposit_label.grid(row=0, column=0, padx=10, pady=10)

        self.deposit_var = tk.StringVar()
        self.deposit_entry = ttk.Entry(self.master, textvariable=self.deposit_var)
        self.deposit_entry.grid(row=0, column=1, padx=10, pady=10)

        self.submit_button = ttk.Button(self.master, text="Submit", command=self.show_deposit_result)
        self.submit_button.grid(row=1, column=0, columnspan=2, pady=10)

    def show_deposit_result(self):
        deposit = int(self.deposit_var.get())
        result = self.acc.deposit_detail(deposit)
        self.show_result_page(result)

    def show_result_page(self, result):
        self.clear_window()

        result_label = ttk.Label(self.master, text=result)
        result_label.grid(row=0, column=0, padx=10, pady=10)

        back_button = ttk.Button(self.master, text="Back to Home", command=self.show_home_page)
        back_button.grid(row=1, column=0, columnspan=2, pady=10)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

class Account:
    rate_of_interest = 0

    def __init__(self):
        self.balance = 50000
        self.account_number = 26382827123

    def show_balance(self):
        return f"Balance: {self.balance}"

    def show_rate_of_interest(self, rate, time):
        self.rate_of_interest = (self.balance * rate * time) / 100
        return f"Rate of Interest: {self.rate_of_interest}"

    def withdrawal_detail(self, withdrawal=0):
        self.balance -= withdrawal
        return f"Balance after withdrawal {withdrawal} ==>> {self.balance}"

    def deposit_detail(self, deposit=0):
        self.balance += deposit
        return f"Balance after deposit {deposit} ==>> {self.balance}"

if __name__ == "__main__":
    root = tk.Tk()
    app = AccountGUI(root)
    root.mainloop()
