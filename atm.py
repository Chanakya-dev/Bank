class Account:
    def __init__(self, holder, balance, pin):
        self.holder = holder
        self.balance = balance
        self.pin = pin

    def check_balance(self):
        print("Current Balance: $" + str(round(self.balance, 2)))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("$" + str(round(amount, 2)) + " deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount, pin):
        if pin != self.pin:
            print("Invalid PIN. Transaction denied.")
        elif amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print("$" + str(round(amount, 2)) + " withdrawn successfully.")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin and len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Invalid PIN or new PIN is not valid.")

    def __str__(self):
        return f"Account Holder: {self.holder}, Balance: ${round(self.balance, 2)}"


def atm_menu(account):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. View Account Info")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            pin = input("Enter your PIN: ")
            account.withdraw(amount, pin)
        elif choice == "4":
            old_pin = input("Enter your current PIN: ")
            new_pin = input("Enter your new PIN: ")
            account.change_pin(old_pin, new_pin)
        elif choice == "5":
            print(account) 
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    account = Account("John Doe", 1000.00, "1234")
    print(f"Welcome, {account.holder}!")
    atm_menu(account)
