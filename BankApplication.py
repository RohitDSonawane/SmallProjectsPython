import datetime

class Transaction:
    def __init__(self, txn_type, amount, balance_after):
        self.txn_type = txn_type
        self.amount = amount
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.balance_after = balance_after

    def __str__(self):
        return f"{self.date} | {self.txn_type:<10} | ₹{self.amount:<10} | Balance: ₹{self.balance_after}"

class Account:
    def __init__(self, name, address, age):
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")

        self.name = name
        self.address = address
        self.age = age
        self.balance = 0.0
        self.transactions = []

    def update_address(self, new_address):
        self.address = new_address

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount, self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.transactions.append(Transaction("Withdraw", amount, self.balance))

    def get_balance(self):
        return self.balance

    def get_statement(self):
        return [str(txn) for txn in self.transactions]

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_id, name, address, age):
        if acc_id in self.accounts:
            raise KeyError("Account ID already exists.")
        self.accounts[acc_id] = Account(name, address, age)
        print(f"Account created for {name} with ID {acc_id}")

    def update_account(self, acc_id, new_address):
        self._get_account(acc_id).update_address(new_address)
        print("Address updated.")

    def deposit(self, acc_id, amount):
        self._get_account(acc_id).deposit(amount)
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, acc_id, amount):
        self._get_account(acc_id).withdraw(amount)
        print(f"₹{amount} withdrawn successfully.")

    def display_balance(self, acc_id):
        balance = self._get_account(acc_id).get_balance()
        print(f"Current balance: ₹{balance}")

    def display_statement(self, acc_id):
        print("Transaction History:")
        for txn in self._get_account(acc_id).get_statement():
            print(txn)

    def _get_account(self, acc_id):
        if acc_id not in self.accounts:
            raise KeyError("Account ID not found.")
        return self.accounts[acc_id]

# --- Interactive Menu (CLI) ---

def main():
    bank = Bank()

    while True:
        print("\n=== BANKING SYSTEM MENU ===")
        print("1. Create Account")
        print("2. Update Address")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Display Balance")
        print("6. Display Statement")
        print("0. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                acc_id = input("Enter Account ID: ")
                name = input("Enter Account Holder Name: ")
                address = input("Enter Address: ")
                age = int(input("Enter Age: "))
                bank.create_account(acc_id, name, address, age)

            elif choice == '2':
                acc_id = input("Enter Account ID: ")
                new_address = input("Enter New Address: ")
                bank.update_account(acc_id, new_address)

            elif choice == '3':
                acc_id = input("Enter Account ID: ")
                amount = float(input("Enter amount to deposit: "))
                bank.deposit(acc_id, amount)

            elif choice == '4':
                acc_id = input("Enter Account ID: ")
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(acc_id, amount)

            elif choice == '5':
                acc_id = input("Enter Account ID: ")
                bank.display_balance(acc_id)

            elif choice == '6':
                acc_id = input("Enter Account ID: ")
                bank.display_statement(acc_id)

            elif choice == '0':
                print("Thank you for using the banking system!")
                break

            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
