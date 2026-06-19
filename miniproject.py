import sys
class customer:
    bank_name = "state bank of india"
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance


    def deposit(self,amt):
        self.balance += amt
        print(f'balance after deposit :{self.balance}')

    def withdraw(self,amt):
        if amt > self.balance:
            print(f'insufficient funds .. cannot perform this operation')
            return
        self.balance -= amt
        print(f'balance after withdraw: {self.balance}')
print(f'welcome to {customer.bank_name}')
name = input('enter your name: ')
c = customer(name)
while True:
    print('\nd-deposit\nw-withdraw\ne-exit')
    option = input("choose your option:").lower()
    if option == 'd':
        amt = float(input("enter amount:"))
        c.deposit(amt)
    elif option == 'w':
        amt = float(input("enter amount:"))
        c.withdraw(amt)
    elif option == 'e':
        print("thank you for using our banking services")
        
        sys.exit()
    else:
        print("invalid option... please try again")