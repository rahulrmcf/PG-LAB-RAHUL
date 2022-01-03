class bank:
    def __init__(self,acno,name,atype,bal=0):
        self.acno=acno
        self.name=name
        self.atype=atype
        self.bal=bal
    def deposit(self,bal):
        self.bal=self.bal+bal
    def withdraw(self,bal):
        if(self.bal==0):
            print("Insufficient balance!")
        else:
            self.bal=self.bal-bal
    def display(self):
        print("Name: ",self.name)
        print("AC No : ",self.acno)
        print("Account typle: ",self.atype)
        print("Balance amount: ",self.bal)

acno=int(input("Enter the account number: "))
name=input("Enter the customer name: ")
atype=input("Enter the account type(Savings/Current): ")
bn=bank(acno,name,atype)
while(True):
    print("ENTER YOUR CHOICE")
    print()
    print("1.Withdraw")
    print("2.Deposit")
    print("3.Display")
    print("4.Exit")
    c=int(input())
    if(c==1):
        a=int(input("Enter the amount to withdraw: "))
        bn.withdraw(a)
    if(c==2):
        a2=int(input("Enter the amount to deposit: "))
        bn.deposit(a2)
    if(c==3):
        bn.display()
    if(c==4):
        break
