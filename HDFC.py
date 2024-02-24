class HDFC:
    ROI=9.5  #rate of interest  #class variable

    def __init__(self,Name,Amount):  #Constructor
        self.AccountHolder=Name     #Instance variable
        self.Balance=Amount         #Instance variable
        print("Welcome",self.AccountHolder)
        print("Account gets successfully created with initial balance:",self.Balance)

    def DisplayBalance(self):       #Instance method
        print("Hello",self.AccountHolder)
        print("Your account balance is :",self.Balance)

    @classmethod
    def DisplayBankInfo(cls):       #class method
        print("Welcome to HDFC bank portal")
        print("Our Bank is Private LTD Bank")
        print("We provide the Rate of Intrest on saving account is:",cls.ROI)

    @staticmethod
    def DisplayKYCInfo():
        print("Account to the rules of RBI you should be provide below documents for KYC")
        print("Your Aadhar card")
        print("Your PAN card")
        print("Your passport size photo")

    def withdrawl(self,Amount):       #Instance method
        if self.Balance < Amount:
            print("There is no sufficient balance")
        else:
            self.Balance=self.Balance-Amount
            print("Amount withdrawl successfully ....")
    
    def Deposit(self,Amount):       #Instance method
        self.Balance=self.Balance+Amount
        print("Amount deposited successfully...")


def main():
    print("Rate of Interest of HDFC Bank is:",HDFC.ROI)

    HDFC.DisplayBankInfo()

    print("Creating new account....")
    Amit=HDFC("Amit",5000)     #__init__(100,"Amit",5000)
    print("Creating new account....")
    Sagar=HDFC("Sagar",3000)     #__init__(200,"Sagar",3000)

    print("Performing operations on Amit's Account")
    Amit.Deposit(2000)
    Amit.DisplayBalance()

    Amit.withdrawl(1000)
    Amit.DisplayBalance()

    print("Performing operations on Sagar's Account")
    Sagar.Deposit(4000)
    Sagar.DisplayBalance()

    Sagar.withdrawl(500)
    Sagar.DisplayBalance()

    HDFC.DisplayKYCInfo()


if __name__=="__main__":
    main()