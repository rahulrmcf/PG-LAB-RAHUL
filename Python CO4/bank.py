class bank:
    def __init__(self,acno,name,atype,bal=0):
        self.acno=acno
        self.name=name
        self.atype=atype
        self.bal=bal
    def deposit(self,bal):
        self.bal=self.bal+bal
    def withdraw(self,bal):
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
a=int(input("Enter the amount to deposit: "))
bn.deposit(a)
a2=int(input("Enter the amount to withdraw: "))
bn.withdraw(a2)
bn.display()
