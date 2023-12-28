import pandas as pd
import random
import sys


class BankSystem:
    def __init__(self):
        self.accounts_df = pd.DataFrame(columns=['Customer_name', 'Account_number', 'Pin', 'Balance'])
        self.logged_in_user = None

    def create_account(self, user_name, user_pin):
        account_num = int(random.randint(1000000000, 9999999999))  # Generate a 10-digit account number
        balance = 0
        new_account = {'Customer_name': user_name, 'Account_number': account_num, 'Pin': user_pin, 'Balance': balance}
        self.accounts_df.loc[len(self.accounts_df)] = new_account
        print(f"Account created successfully! Your account number is: {account_num}")

    def login(self, account_no, user_pin):
        account_no = int(account_no)
        user_pin = str(user_pin).strip()

        if account_no in self.accounts_df['Account_number'].values:
            if self.accounts_df.loc[self.accounts_df['Account_number'] == account_no, 'Pin'].values[0] == user_pin:
                self.logged_in_user = account_no
                print("Login successful!")
            else:
                print("Invalid account number or PIN. Login failed.")

    def check_balance(self):
        if self.logged_in_user is not None:
            balance = self.accounts_df.loc[self.accounts_df['Account_number'] == self.logged_in_user, 'Balance'].values[
                0]
            print(f"Your current balance is: Rs.{balance}")
        else:
            print("Please log in first.")

    def withdraw(self, amount):
        if self.logged_in_user is not None:
            current_balance = \
                self.accounts_df.loc[self.accounts_df['Account_number'] == self.logged_in_user, 'Balance'].values[0]
            if amount <= current_balance:
                new_balance = current_balance - amount
                self.accounts_df.loc[self.accounts_df['Account_number'] == self.logged_in_user, 'Balance'] = new_balance
                print(f"Withdrawal successful! New balance: ${new_balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Please log in first.")

    def deposit(self, amount):
        if self.logged_in_user is not None:
            current_balance = \
                self.accounts_df.loc[self.accounts_df['Account_number'] == self.logged_in_user, 'Balance'].values[0]
            new_balance = current_balance + amount
            self.accounts_df.loc[self.accounts_df['Account_number'] == self.logged_in_user, 'Balance'] = new_balance
            print(f"Deposit successful! New balance: ${new_balance}")
        else:
            print("Please log in first.")


# Example Usage:
bank_system = BankSystem()

while True:
    print("\n1. Create Account\n2. Login\n3. Check Balance\n4. Withdraw\n5. Deposit\n6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        customer_name = input("Enter your name: ")
        pin = input("Create your PIN: ")
        bank_system.create_account(customer_name, pin)

    elif choice == '2':
        account_number = int(input("Enter your account number: "))
        pin = input("Enter your PIN: ")
        bank_system.login(account_number, pin)

    elif choice == '3':
        bank_system.check_balance()

    elif choice == '4':
        amount = float(input("Enter the withdrawal amount: $"))
        bank_system.withdraw(amount)

    elif choice == '5':
        amount = float(input("Enter the deposit amount: $"))
        bank_system.deposit(amount)

    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
