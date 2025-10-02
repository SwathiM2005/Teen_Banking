class account:
    def __init__(self,name,accountnum,balance):
        self.name=name
        self.accountnum=accountnum
        self.balance=balance


    def deposit(self,amount):
        if amount<0:
            print("invliad..cannot be deposited")
        else:
            self.balance+=amount
            print(f"{amount}has been deposited.Current Balance is{self.balance}")

    def withdraw(self,amount):
        if amount<0:
            print("Amount cannot be withdrawn")
        elif self.balance<amount:
            print("insufficient balance")
        else:
            print(f"The amount{amount}has been withdrawn")
            self.balance-=amount
            print(f"The balance is{self.balance}")

    def checkbalance(self):
        if self.balance<500:
            print("please maintain minimum balance")
        else:
            print(f"The current balance is{self.balance}")


print("welcome to teenbank")
name=input("Enter the name:")
accountnum=int(input("enter the number:"))
balance=float(input("Enter the balance:"))
Account=account(name,accountnum,balance)
while True:
    print("1->deposit")
    print("2->withdraw")
    print("3->checkbalance")
    print("4->exit")

    choice=input("Enter yout choice")

    if choice=="1":
        print("Enter the amount to deposit:")
        amount=int(input("Enter the amount:"))
        Account.deposit(amount)

    elif choice=="2":
        print("Enter the amount to withdraw:")
        amount=int(input("Enter the amount:"))
        Account.withdraw(amount)

    elif choice=="3":
        Account.checkbalance()

    elif choice=="4":
        exit(0)

    else:
        print("Invalid choice")
        
    

    
            





