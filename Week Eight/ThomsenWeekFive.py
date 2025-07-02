# imports
import random

# class for account creation and management
class Account:

    # initialize account with account number, owner's name, SSN, PIN, and balance (of 0)
    def __init__(self, account_number, first_name, last_name, ssn, pin):
        self.account_number = account_number
        self.owner_first_name = first_name
        self.owner_last_name = last_name
        self.ssn = ssn
        self.pin = pin
        self.balance = 0

    # method for depositing money into the account
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # method for withdrawing money from the account
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"\033[31mInsufficient funds in account {self.account_number}\033[0m")
            return self.balance
        self.balance -= amount
        return self.balance

    # method to check if the provided PIN matches the account's PIN
    def isValidPIN(self, input_pin):
        return self.pin == input_pin

    # method to return a string representation of the account
    def __str__(self):
        masked_ssn = f"XXX-XX-{self.ssn[-4:]}"
        return (f"\033[35m============================================================\033[0m\n"
                f"\033[36mAccount Number: {self.account_number}\n"
                f"Owner First Name: {self.owner_first_name}\n"
                f"Owner Last Name: {self.owner_last_name}\n"
                f"Owner SSN: {masked_ssn}\n"
                f"PIN: {self.pin}\n"
                f"Balance: ${self.balance / 100:.2f}\033[0m\n"
                f"\033[35m============================================================\033[0m")

# class for managing the bank and its accounts
class Bank:
    # maximum number of accounts allowed in the bank
    MAX_ACCOUNTS = 100

    # initialize the bank with an empty list of accounts
    def __init__(self):
        self.accounts = []

    # method to add an account to the bank
    def addAccountToBank(self, account):
        if len(self.accounts) >= self.MAX_ACCOUNTS:
            print("\033[33mNo more accounts available\033[0m")
            return False
        self.accounts.append(account)
        return True

    # method to remove an account from the bank
    def removeAccountFromBank(self, account):
        for i, acc in enumerate(self.accounts):
            if acc.account_number == account.account_number:
                self.accounts.pop(i)
                return True
        return False

    # method to find an account by its account number
    def findAccount(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    # method to add monthly interest to all accounts
    def addMonthlyInterest(self, rate):
        monthly_rate = rate / 12 / 100
        for account in self.accounts:
            interest = int(account.balance * monthly_rate)
            account.deposit(interest)
            print(f"\033[32mDeposited interest: ${interest / 100:.2f} into account number: {account.account_number}, "
                  f"new balance: ${account.balance / 100:.2f}\033[0m")

# class for storing and parsing coin values
class CoinCollector:
    coin_values = {'P': 1, 'N': 5, 'D': 10, 'Q': 25, 'H': 50, 'W': 100}

    # method to parse a string of coins and calculate the total value
    @staticmethod
    def parseChange(coins):
        total = 0
        for coin in coins:
            if coin.upper() in CoinCollector.coin_values:
                total += CoinCollector.coin_values[coin.upper()]
            else:
                print(f"\033[31mInvalid coin: {coin}\033[0m")
        return total

# class for utility functions related to the bank
class BankUtility:

    # method to prompt the user for a string input
    @staticmethod
    def promptUserForString(prompt):
        return input(prompt)

    # method to prompt the user for a positive number
    @staticmethod
    def promptUserForPositiveNumber(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print("\033[31mAmount cannot be negative. Try again.\033[0m")
                    continue
                return value
            except ValueError:
                print("\033[31mInvalid number. Try again.\033[0m")

    # method to convert a dollar amount to cents
    @staticmethod
    def convertFromDollarsToCents(amount):
        return int(round(amount * 100))

    # method to generate a random integer 
    @staticmethod
    def generateRandomInteger(minimum, maximum):
        return random.randint(minimum, maximum)

    # method to check if a string is numeric
    @staticmethod
    def isNumeric(string):
        return string.isdigit()

# function to prompt for account number and PIN, returning the account if valid
def promptForAccountNumberAndPIN(bank):
    try:
        account_number = int(input("\033[35mEnter account number:\033[0m\n"))
        account = bank.findAccount(account_number)
        if not account:
            print(f"\033[31mAccount not found for account number: {account_number}\033[0m")
            return None
        pin = input("\033[35mEnter PIN:\033[0m\n")
        if not account.isValidPIN(pin):
            print("\033[31mInvalid PIN\033[0m")
            return None
        return account
    except ValueError:
        print("\033[31mInvalid account number format.\033[0m")
        return None

# main function to run the bank application
def main():
    # initialize the bank
    bank = Bank()
    
    # main loop for user interaction
    while True:
        print("\033[35m============================================================\033[0m")
        print("\033[35mWhat do you want to do?\033[0m")
        print("1. Open an account")
        print("2. Get account information and balance")
        print("3. Change PIN")
        print("4. Deposit money in account")
        print("5. Transfer money between accounts")
        print("6. Withdraw money from account")
        print("7. ATM withdrawal")
        print("8. Deposit change")
        print("9. Close an account")
        print("10. Add monthly interest to all accounts")
        print("11. End Program")
        print("\033[35m============================================================\033[0m")
        choice = input("\033[35mEnter choice: \033[0m")

        # option one for opening an account
        if choice == "1":
            first = input("\033[35mEnter Account Owner's First Name:\033[0m\n")
            last = input("\033[35mEnter Account Owner's Last Name:\033[0m\n")
            ssn = input("\033[35mEnter Account Owner's SSN (9 digits):\033[0m\n")
            if len(ssn) != 9 or not ssn.isdigit():
                print("\033[31mSocial Security Number must be 9 digits\033[0m")
                continue
            while True:
                account_number = BankUtility.generateRandomInteger(10000000, 99999999)
                if bank.findAccount(account_number) is None:
                    break
            pin = str(BankUtility.generateRandomInteger(0, 9999)).zfill(4)
            new_account = Account(account_number, first, last, ssn, pin)
            bank.addAccountToBank(new_account)
            print("\033[32mAccount successfully created!\033[0m")
            print(new_account)

        # option two for getting account information and balance
        elif choice == "2":
            account = promptForAccountNumberAndPIN(bank)
            if account:
                print(account)

        # option three for changing PIN
        elif choice == "3":
            account = promptForAccountNumberAndPIN(bank)
            if account:
                while True:
                    new_pin = input("\033[35mEnter new PIN:\033[0m\n")
                    if not BankUtility.isNumeric(new_pin) or len(new_pin) != 4:
                        print("\033[31mPIN must be 4 digits, try again.\033[0m")
                        continue
                    confirm_pin = input("\033[35mEnter new PIN again to confirm:\033[0m\n")
                    if new_pin != confirm_pin:
                        print("\033[31mPINs do not match, try again.\033[0m")
                        continue
                    account.pin = new_pin
                    print("\033[32mPIN updated\033[0m")
                    break

        # option four for depositing money in account
        elif choice == "4":
            account = promptForAccountNumberAndPIN(bank)
            if account:
                amount = BankUtility.promptUserForPositiveNumber("\033[35mEnter amount to deposit in dollars and cents (e.g. 2.57):\033[0m\n")
                cents = BankUtility.convertFromDollarsToCents(amount)
                account.deposit(cents)
                print(f"\033[32mNew balance: ${account.balance / 100:.2f}\033[0m")

        # option five for transferring money between accounts
        elif choice == "5":
            print("\033[35mAccount to Transfer From:\033[0m")
            from_account = promptForAccountNumberAndPIN(bank)
            if not from_account:
                continue
            print("\033[35mAccount to Transfer To:\033[0m")
            to_account = promptForAccountNumberAndPIN(bank)
            if not to_account:
                continue
            amount = BankUtility.promptUserForPositiveNumber("\033[35mEnter amount to transfer in dollars and cents (e.g. 2.57):\033[0m\n")
            cents = BankUtility.convertFromDollarsToCents(amount)
            if from_account.balance < cents:
                print(f"\033[31mInsufficient funds in account {from_account.account_number}\033[0m")
                continue
            from_account.withdraw(cents)
            to_account.deposit(cents)
            print("\033[32mTransfer Complete\033[0m")
            print(f"\033[32mNew balance in account:{from_account.account_number} is: ${from_account.balance / 100:.2f}\033[0m")
            print(f"\033[32mNew balance in account:{to_account.account_number} is: ${to_account.balance / 100:.2f}\033[0m")

        # option six for withdrawing money from account
        elif choice == "6":
            account = promptForAccountNumberAndPIN(bank)
            if account:
                amount = BankUtility.promptUserForPositiveNumber("\033[35mEnter amount to withdraw in dollars and cents (e.g. 2.57):\033[0m\n")
                cents = BankUtility.convertFromDollarsToCents(amount)
                account.withdraw(cents)
                print(f"\033[32mNew balance: ${account.balance / 100:.2f}\033[0m")

        # option seven for ATM withdrawal
        elif choice == "7":
            account = promptForAccountNumberAndPIN(bank)
            if account:
                try:
                    amount = int(input("\033[35mEnter amount to withdraw in whole dollars (multiples of $5, max $1000):\033[0m\n"))
                    if amount < 5 or amount > 1000 or amount % 5 != 0:
                        print("\033[31mInvalid amount. Try again.\033[0m")
                        continue
                    cents = amount * 100
                    if account.balance < cents:
                        print(f"\033[31mInsufficient funds in account {account.account_number}\033[0m")
                        continue
                    twenties = amount // 20
                    tens = (amount % 20) // 10
                    fives = (amount % 10) // 5
                    account.withdraw(cents)
                    print(f"\033[36m$20 bills: {twenties}, $10 bills: {tens}, $5 bills: {fives}\033[0m")
                    print(f"\033[32mNew balance: ${account.balance / 100:.2f}\033[0m")
                except ValueError:
                    print("\033[31mInvalid input. Try again.\033[0m")

        # option eight for depositing change
        elif choice == "8":
            account = promptForAccountNumberAndPIN(bank)
            if account:
                coins = input("\033[35mDeposit coins (e.g., PNDQHW): \033[0m")
                total = CoinCollector.parseChange(coins)
                account.deposit(total)
                print(f"\033[32m${total / 100:.2f} in coins deposited into account\033[0m")
                print(f"\033[32mNew balance: ${account.balance / 100:.2f}\033[0m")

        # option nine for closing an account
        elif choice == "9":
            account = promptForAccountNumberAndPIN(bank)
            if account:
                bank.removeAccountFromBank(account)
                print(f"\033[32mAccount {account.account_number} closed\033[0m")

        # option ten for adding monthly interest to all accounts
        elif choice == "10":
            rate = BankUtility.promptUserForPositiveNumber("\033[35mEnter annual interest rate percentage:\033[0m\n")
            bank.addMonthlyInterest(rate)

        # option eleven for ending the program
        elif choice == "11":
            print("\033[36mExiting program...\033[0m")
            break

        else:
            print("\033[31mInvalid choice\033[0m")

if __name__ == "__main__":
    main()
