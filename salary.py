salary=int(input("Enter your salary:"))
age=int(input("Enter your age:"))
if(salary>=20000 or age<=25):
    loan=int(input("Enter your loan amount"))
    if(loan>50000):
             print("maximum amount is 50000")
    else:
        print("you are eligible")
else:
    print("you are not eligible")
