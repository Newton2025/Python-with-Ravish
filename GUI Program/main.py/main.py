from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

class AccountGUI(BoxLayout):
    def __init__(self, **kwargs):
        super(AccountGUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.acc = Account()
        self.show_home_page()

    def show_home_page(self):
        self.clear_widgets()

        balance_label = Label(text=f"Balance: ${self.acc.balance}")
        self.add_widget(balance_label)

        action_label = Label(text="Select an action:")
        self.add_widget(action_label)

        actions = ["Show Balance", "Show Interest", "Withdrawal", "Deposit", "Exit"]
        action_dropdown = Spinner(text=actions[0], values=actions)
        self.add_widget(action_dropdown)

        submit_button = Button(text="Submit", on_press=self.show_selected_page)
        self.add_widget(submit_button)

    def show_selected_page(self, instance):
        user_choice = instance.text

        if user_choice == "Show Balance":
            self.show_home_page()
        elif user_choice == "Show Interest":
            self.show_interest_page()
        elif user_choice == "Withdrawal":
            self.show_withdrawal_page()
        elif user_choice == "Deposit":
            self.show_deposit_page()
        elif user_choice == "Exit":
            App.get_running_app().stop()

    def show_interest_page(self):
        self.clear_widgets()

        rate_label = Label(text="Enter rate:")
        self.add_widget(rate_label)

        rate_entry = TextInput(multiline=False)
        self.add_widget(rate_entry)

        time_label = Label(text="Enter time period:")
        self.add_widget(time_label)

        time_entry = TextInput(multiline=False)
        self.add_widget(time_entry)

        submit_button = Button(text="Submit", on_press=self.show_interest_result)
        self.add_widget(submit_button)

    def show_interest_result(self, instance):
        rate = float(self.children[1].text)
        time = int(self.children[3].text)
        result = self.acc.show_rate_of_interest(rate, time)
        self.show_result_page(result)

    def show_withdrawal_page(self):
        self.clear_widgets()

        withdrawal_label = Label(text="Enter Amount to withdraw:")
        self.add_widget(withdrawal_label)

        withdrawal_entry = TextInput(multiline=False)
        self.add_widget(withdrawal_entry)

        submit_button = Button(text="Submit", on_press=self.show_withdrawal_result)
        self.add_widget(submit_button)

    def show_withdrawal_result(self, instance):
        withdrawal = int(self.children[1].text)
        result = self.acc.withdrawal_detail(withdrawal)
        self.show_result_page(result)

    def show_deposit_page(self):
        self.clear_widgets()

        deposit_label = Label(text="Enter Amount to deposit:")
        self.add_widget(deposit_label)

        deposit_entry = TextInput(multiline=False)
        self.add_widget(deposit_entry)

        submit_button = Button(text="Submit", on_press=self.show_deposit_result)
        self.add_widget(submit_button)

    def show_deposit_result(self, instance):
        deposit = int(self.children[1].text)
        result = self.acc.deposit_detail(deposit)
        self.show_result_page(result)

    def show_result_page(self, result):
        self.clear_widgets()

        result_label = Label(text=result)
        self.add_widget(result_label)

        back_button = Button(text="Back to Home", on_press=self.show_home_page)
        self.add_widget(back_button)

    def clear_widgets(self):
        for widget in self.children:
            self.remove_widget(widget)

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

class MyApp(App):
    def build(self):
        return AccountGUI()

if __name__ == "__main__":
    MyApp().run()
