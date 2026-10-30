day = int(input("Enter the day no: "))

match day:
    case 1 | 7:
        print("Weekend")
    case 2:
        print("Start of Weekday")
    case _:
        print("Weekday")
