
class Account:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return f"You have ${self.balance} in your account."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew: ${amount}"
        else:
            return "Amount entered is greater than the balance"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount}."
        else:
            return "Invalid amount."

    @staticmethod
    def change_pin(new, confirm):
        if new == confirm:
            return "Pin changed successfully"
        else:
            return "PINs do not match. Try again."


class ATM:
    def __init__(self):
        self.users = {"user1": {1001: 10000}, "user2": {1002: 20000},
                      "user3": {1003: 30000}, "user4": {1004: 40000},
                      "user5": {1005: 50000}}

    def display_menu(self):
        print("\nSelect from the following options: ")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

    def choosing(self, user, pin, account):
        while True:
            self.display_menu()
            choice = int(input("Enter the option number you want to choose: "))

            if choice == 1:
                print(account.get_balance())
            elif choice == 2:
                amount = float(input("Enter amount to deposit: "))
                print(account.deposit(amount))
                self.users[user][pin] = account.balance
            elif choice == 3:
                amount = float(input("Enter amount to withdraw: "))
                print(account.withdraw(amount))
                self.users[user][pin] = account.balance
            elif choice == 4:
                new_pin = int(input("Enter new PIN: "))
                confirm_pin = int(input("Confirm new PIN: "))
                result = Account.change_pin(new_pin, confirm_pin)
                print(result)
                if result == "Pin changed successfully":
                    self.users[user][new_pin] = self.users[user].pop(pin)
                    self.users[user] = new_pin
            elif choice == 5:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def authenticate(self):
        u1 = input("Enter user name: ")
        if u1 not in self.users:
            print("Invalid User!")
        else:
            print()
            pin = int(input("Enter your PIN: "))
            if pin not in self.users[u1]:
                print("Invalid PIN. Access denied.")
                print()
                self.authenticate()
            else:
                print("Access granted!")
                print()
                print(f"Welcome, {u1}")
                print(f"You have {self.users[u1][pin]}")
                balance = self.users[u1][pin]
                account = Account(balance)
                self.choosing(u1, pin, account)


ur_atm = ATM()
ur_atm.authenticate()
