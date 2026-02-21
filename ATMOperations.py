#ATMOperations.py <-- Module Name
from ATMExcept import *
bal = 500.00 #Global Amount
def deposit():
    damt=float(input("Enter Your Deposit Amount:"))
    print("-" * 20)
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Your Account XXXXXXXXX123 Credited With INR:{}".format(damt))
        print("-" * 20)
        print("Your Account XXXXXXXXX123 Current Balance INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter Your Withdraw Amount:"))
    print("-" * 20)
    if(wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("Your Account XXXXXXXXX123 Debited With INR:{}".format(wamt))
        print("-" * 20)
        print("Your Account XXXXXXXXX123 Current Balance INR:{}".format(bal))
def balenq():
    print("-" * 20)
    print("Your Account XXXXXXXXX123 Total Balance INR:{}".format(bal))