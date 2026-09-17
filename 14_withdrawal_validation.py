Balance = float(input("Enter your Balance : "))
Withdrawal = float(input("Enter your withdrawal amount : "))

if Withdrawal <=0:
    print("Invaild Amount....")

elif Withdrawal > Balance:
    print("Insufficient Balance")

else :
    print("Withdrawal Success....")
    print("New Balance:",Balance - Withdrawal)
