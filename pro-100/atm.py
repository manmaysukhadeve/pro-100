class atm:
    def __init__(self,CashWithdrawl,BalanceEnquiry,CashDeposit):
        self.CashWithdrawal = CashWithdrawl
        self.BalanceEnquiry = BalanceEnquiry
        self.CashDeposit = CashDeposit

    def getCashWithdrawal(self,):
        print("Enter your amount")



Manmay = atm (1000,2500,100)


print("CashWihrawal",Manmay.CashWithdrawal)
print("BalanceEnquiry",Manmay.BalanceEnquiry)
print("CashDeposit",Manmay.CashDeposit)