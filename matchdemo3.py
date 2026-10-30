print("CHOOSE THE OPERATION:\n + -> ADDITION\n - => SUBTRACTION\n * -> MULTIPLICATION\n / -> DIVISION ")
op=input("enter the operation")
match op:
    case "+":
        a=int(input("ENTER A VALUE:"))
        b=int(input("ENTER b VALUE:"))
        print("ADDITION OD A AND B:",a+b)
    case "-":
        a=int(input("ENTER A VALUE:"))
        b=int(input("ENTER b VALUE:"))
        print("ADDITION OD A AND B:",a-b)
    case "*":
        a=int(input("ENTER A VALUE:"))
        b=int(input("ENTER b VALUE:"))
        print("ADDITION OD A AND B:",a*b)
    case "/":
        a=int(input("ENTER A VALUE:"))
        b=int(input("ENTER b VALUE:"))
        print("ADDITION OD A AND B:",a/b)
    case _:
        print("INVALID OPERATION")
        
