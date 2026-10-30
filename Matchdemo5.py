number = int(input("Enter the number"))

match number:
    case n if n >10:
        print("Greater than 10")
    case _:
        print("Lesser than 10")
