class BankATM:
    def deposit(self, balance, amount):
        if amount > 0:
            balance += amount
            print(f"Deposit of {amount} successful.")
        else:
            print("Invalid deposit amount.")
        return balance

    def withdraw(self, balance, amount):
        if amount > 0:
            if balance >= amount:
                balance -= amount
                print(f"Withdrawal of {amount} successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")
        return balance

    def check_balance(self, balance):
        print(f"Current balance: {balance}")


# Creating an instance of the BankATM class
atm = BankATM()

# ATM menu function
def atm_menu(balance):
    while True:
        print("\nBank ATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            atm.check_balance(balance)
        elif choice == '2':
            amount = float(input("Enter the deposit amount: "))
            balance = atm.deposit(balance, amount)
        elif choice == '3':
            amount = float(input("Enter the withdrawal amount: "))
            balance = atm.withdraw(balance, amount)
        elif choice == '4':
            print("Thank you for using the bank ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Running the ATM menu
initial_balance = 0
atm_menu(initial_balance)
