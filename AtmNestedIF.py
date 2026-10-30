bill = int(input("Enter the bill amount"))
member = False

if bill > 5000:
    if member:
     discount = bill * 0.20
     finalBill = bill - discount 
    else:
     discount = bill * 0.10
     finalBill = bill - discount
elif member:
     discount = bill * 0.05
     finalBill = bill - discount  
else:
    finalBill = bill

print("The Final Bill amount is",finalBill)
