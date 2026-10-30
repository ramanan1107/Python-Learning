units = int(input("Enter the units: "))

if units<=100:
    bill = units * 2
elif units<=200:
    bill = (100*2)+ ((units-100)*3)
elif units<=300:
    bill = (100*2) + (100*3) +((units-200)*5)
else:
    bill = (100*2) + (100*3) +((units-200)*5)

print("Your bill: "+ str(bill))
