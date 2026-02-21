#ATMmaiProject.py <-- Main Program
from ATMMenu import menu
from ATMOperations import*
try:
    while(True):
        menu()
        ch=int(input("Enter Your Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("-"*20)
                    print("\tDon't Try To Deposit -VE / Zero value-try again ")
                except ValueError:
                    print("-" * 20)
                    print("\tDon't Try To Deposit Alnums, Strs, and Symbols-Try Again")
            case 2:
                try:
                    withdraw()
                except WithdrawError:
                    print("-" * 20)
                    print("\tDon't Try To Withdraw -VE / Zero value-try again ")
                except InSuffFundError:
                    print("-" * 20)
                    print("\tYour Account Dose Not Have Enough Funds To Withdraw")
                except ValueError:
                    print("-" * 20)
                    print("\tDon't Try To Withdraw Alnums, Strs, and Symbols-Try Again")
            case 3:
                balenq()
            case 4:
                print("-" * 20)
                print("\tThanks For Using This Project")
                break
            case _:
                print("-"*20)
                print("\tYour Selection Of Operation Is Wrong-Try Again")
except ValueError:
    print("-"*20)
    print("Don't Enter Alnums, Strs, and Symbols For Choice Try-Again:")
