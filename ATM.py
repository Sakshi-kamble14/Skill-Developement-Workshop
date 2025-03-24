class ATM():
    def __init__ (self,balance=1000):
         self.balance=balance
    def checkbalance(self):
        print("Your current balance is:",self.balance)
    def depositAmount(self,amount):
        self.balance+=self.amount
        return self.balance

print("WELCOME TO OUR ATM MACHINE SYSTEM")

print("MENU=>\n1.Check Balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit the system")

ch=int(input("Enter your choice:"))

if ch==1:
    self.checkbalance()
elif ch==2:
    self.depositAmount(self,5000)