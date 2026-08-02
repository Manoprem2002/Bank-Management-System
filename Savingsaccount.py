class Savings :
    def __init__(self, amount = 0,minimum_hold_value = 500):
        self.amount = amount
        self.minimum_hold_value = minimum_hold_value
    
    def deposit_saving(self, deposit_amount):
        self.amount += deposit_amount
        return print(f"Deposited {deposit_amount}. New saving balance is {self.amount}.")

    def withdraw(self, withdraw_amount):
        if self.amount - withdraw_amount < self.minimum_hold_value:
            return print(f"Cannot withdraw {withdraw_amount}. Minimum hold value is {self.minimum_hold_value}. Current balance is {self.amount}.")
        else:
            self.amount -= withdraw_amount
            return print(f"Withdraw {withdraw_amount}. New balance is {self.amount}.")
    
    def show_saving_balance(self):
        return print(f"Current Savings Account balance is {self.amount}.")