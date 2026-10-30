start = int(input("Enter the start: "))
end = int(input("Enter the end: "))
even = 0
odd = 0

for i in range(start, end+1):
    if i%2 == 0:
        even = even+1
    else:
        odd = odd+1

print("Even count:", even)
print("Odd count:", odd)
