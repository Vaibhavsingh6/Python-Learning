Balance = float(input("Enter Balance :"))
Deposit = float(input("Enter Deposit Amount :"))

if Deposit > 0:
    print("New Balance :", Balance+Deposit)
else:
    print("Invaild Deposit Amount")    