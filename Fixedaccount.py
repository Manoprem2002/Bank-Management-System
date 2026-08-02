class Fixedaccount :
    def __init__(self,fix_amount = 0, intrest_rate = 15):
        self.fix_amount = fix_amount
        self.intrest_rate = intrest_rate
    
    def deposit_fix(self, deposit_fix_amount):
        self.fix_amount += deposit_fix_amount
        return print(f"Deposited {deposit_fix_amount}. New fix balance is {self.fix_amount}.")

    def show_intrest(self):
        intrest = self.fix_amount * (self.intrest_rate / 100)
        return print(f"Intrest earned is {intrest}.")

    def show_fix_balance(self):
        return print(f"Current Fixed Balance is {self.fix_amount}.")