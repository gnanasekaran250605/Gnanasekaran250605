a=int(input("Enter a tamil mark:"))
b=int(input("Enter a english mark:"))
c=int(input("Enter a maths mark"))
d=int(input("Enter a science mark"))
e=int(input("Enter a social mark:"))
f=a+b+c+d+e
average=f/5
if(average<35):
    print("aditional class is required")
else:
    print("you are good to go")
