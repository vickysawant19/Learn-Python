class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self,initialAmount,accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created,\nBalance = '{self.balance:.2f}'")
        
    def getBalance(self):
        print(f"Account '{self.name}' balance = $ {self.balance:.2f}")

    def deposite(self,amount):
        self.balance = self.balance + amount
        print(f"\ndeposite Complete")
        self.getBalance()

    def viableTrasnaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry , account '{self.name}' only has a balnce of '{self.balance:.2f}'"
            )
    def withdrow(self,amount):
        try:
            self.viableTrasnaction(amount)
            self.balance = self.balance - amount
            print(f"withdraw complete")
            self.getBalance()

        except BalanceException as error:
            print(f"\nwithdraw interrupted : {error}")


    def trasnfer(self,amount,account):
        try:
            print(f"***********\n\nBegining transfer..🚀")
            self.viableTrasnaction(amount)
            self.withdrow(amount)
            account.deposite(amount)
            print(f"\nTransfer complted ✅\n\n***********")
        except BalanceException as error:
            print(f"\nTrasfer interrupted: {error}")

class IntrestRewardAcct(BankAccount):
    def deposite(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposite complted.")
        self.getBalance()


class SavingAcct(IntrestRewardAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5
    def withdrow(self, amount):
        try:
            self.viableTrasnaction(amount +self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\nWithdraaw completed')
            self.getBalance()
        except BalanceException as error:
            print(f"'\n Withdraw interrupted:{error}")