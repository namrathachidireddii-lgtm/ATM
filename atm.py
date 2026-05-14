balance = 1000
Pin = 1234

user = int(input("Enter your pin: "))
if user == Pin:
    print("Pin accepted. You can proceed with your transaction.")
else: print("The entered pin is incorrect. Please try again.")

print("====== Welcome to the ATM======")
print("1. Check Balance")
print("2. Deposit")
print("3.Withdraw")
print("4.Exit")
choice = float(input("Enter your choice: "))
if choice == 1:
    print("Your current balance is: ", balance)

elif  choice == 2:
    amount = float(input("Enter the amount to deposit: "))
    balance += amount
    print("Deposit successful. Your new balance is: ", balance)

elif choice == 3:
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds.", balance)
    else:
        balance = balance - amount
        print("Withdrawal successful. Your new balance is: ", balance)
elif choice == 4:
    print("Thank you for using ATM. Goodbye!")
else:
    print("Invalid choice.", balance)
    



