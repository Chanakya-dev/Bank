class BankAccount:
    def __init__(self,name,account_number,IFSC,balance=0,pin=None):
        self.name=name
        self.account_number=account_number
        self.IFSC=IFSC
        self.balance=balance
        self.pin=pin
        
    def deposit(self,amount):
        if(amount>0):
            self.balance+=amount
            return(f"deposited {amount}. New balance is {self.balance}")
        else:
            return("invalid amount deposited")
    def withdraw(self,amount):
        if(0<amount<self.balance):
            self.balance-=amount
            return(f"withdraw {amount}. New balance is {self.balance}")
        else:
            return("Insufficient funds")
    def balance_enquiry(self):
        return(f" Account holder:{self.name}\n account_number:{self.account_number}\n IFSC:{self.IFSC}\n balance:{self.balance}")
    def change_pin(self,current_pin,new_pin):
        if self.pin == current_pin:
            if current_pin != new_pin:
                self.pin = new_pin
                return("PIN changed successfully.")
            else:
                return("New PIN must be different from the current PIN.")
        else:
            return("Current PIN is incorrect.")
        

bank=BankAccount("ram",123456789,"SBIN0001",0,1234)
print(bank.deposit(1000))
print(bank.withdraw(100))
print(bank.balance_enquiry())
print(bank.change_pin(1234,5678))
        
        
    