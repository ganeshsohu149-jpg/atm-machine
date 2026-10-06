balance = 10000
pin = "9001"
history = []

def authenticate():
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN : ")
        if entered_pin == pin:
            print(" Login Successful!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")

    print(" Card blocked due to 3 failed attempts.")
    return False


def check_balance():
    print("f Current Balance: Rs. {balance}")


def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        history.append(f"Deposited: +Rs. {amount}")
        print(f" Successfully deposited Rs. {amount}")
    else:
        print(" Invalid deposit amount!")


def withdraw(amount):
    global balance
    if amount <= 0:
        print(" Invalid withdrawal amount!")
    elif amount > balance:
        print(" Insufficient balance!")
    else:
        balance -= amount
        history.append(f"Withdrawn: -Rs. {amount}")
        print(f" Please collect your cash: Rs. {amount}")


def show_history():
    print("--- Recent Transactions ---")
    if not history:
        print("No transactions yet.")
    else:
        for item in history[-5:]:
            print(item)
    print("---------------------------")


if authenticate():
    while True:
        print("--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            amt = float(input("Enter amount to deposit: "))
            deposit(amt)
        elif choice == "3":
            amt = float(input("Enter amount to withdraw: "))
            withdraw(amt)
        elif choice == "4":
            show_history()
        elif choice == "5":
            print(" Thank you for banking with us. Have a great day!")
            break
        else:
            print(" Invalid choice, please try again.")