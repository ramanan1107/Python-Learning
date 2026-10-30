start = int(input("Enter the start number: ")) #1
end = int(input("Enter the end number: ")) # 20
sum = 0
evenSum = 0
oddSum = 0
evenCount = 0
oddCount = 0
for i in range(start,end+1):
    sum = sum+i
    if(i %2==0):
        evenSum = evenSum+i
        evenCount = evenCount+1
    else:
        oddSum = oddSum +i
        oddCount = oddCount+1
print("Sum of all numbers:",sum)
print("Sum of even numbers:",evenSum)
print("Sum of odd numbers:",oddSum)
print("Count of even numbers:",evenCount)
print("Count of odd numbers:",oddCount)
    

