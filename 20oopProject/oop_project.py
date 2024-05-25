from bank_accounts import *

vicky = BankAccount(1000,"Vicky")
sara = BankAccount(2000,"sara")

vicky.getBalance()
sara.getBalance()

vicky.deposite(200)

vicky.withdrow(10000)
vicky.withdrow(10.10)


vicky.trasnfer(200,sara)

sara.trasnfer(3000,vicky)

jim = IntrestRewardAcct(1000,"jim")

jim.deposite(100)

jim.trasnfer(100,vicky)


blaze = SavingAcct(1000,"Blaze")

blaze.deposite(100)
blaze.getBalance()
blaze.trasnfer(1100,sara)