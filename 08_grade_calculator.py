Marks = int(input("Enter Your Marks : "))

if Marks < 0 or Marks > 100:
    print("Invaild")
elif Marks >= 90 :
    print("A")
elif Marks >= 80 :
    print("B")
elif Marks >= 70:
    print("C") 
elif Marks >= 60:
    print("D")   
else:
    print("F")