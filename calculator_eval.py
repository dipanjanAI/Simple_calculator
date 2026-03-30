def calculator():
    while True:
        num=input("Enter your operation or (quit) to exit ")
        if num.lower()=="quit":
            print("Exiting calculator...")
            break
        try:
            result=eval(num)
            print("Result= ",result)
        except:
                print("Invalid")

calculator()
