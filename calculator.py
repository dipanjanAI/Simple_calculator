print("Choose the operators shown below")
print("+,-,*,/")
choice=input("Enter your choice ")
sum =0
substract =0
product=1
divition =0
num1=float(input("Enter your first number "))
num2=float(input("Enter your Second number "))
while True:
    if choice=="+":
        sum=num1+num2
        print("Addition of two numbers =",sum)
    elif choice=="-":
        substract=num1-num2
        print("Substraction of two numbers =",substract)
    elif choice=="*":
        product=num1*num2
        print("Multiplication of two numbers =",product)
    elif choice=="/":
        divition=num1/num2
        print("Divition of two numbers =",divition)
    else:
        print("Invalid")
    break
        
    
    
