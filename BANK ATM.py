class Atm:
    def __init__(self,cardnumber , pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber
    def return_cardnumber(self):
        print("Do you want to CashWithdrawl or BalanceEnquiry.",self.cardnumber)
    def cashhwithdrawl(self):
        print("Cashwithdrawl")
    def cashSaving(self):
        print("cashSaving")
