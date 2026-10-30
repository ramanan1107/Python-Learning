numbers = [0, 10, 0, 20, 30, 0, 40]
result = []
count = 0
for num in numbers:
    if num ==0:
        count = count+1
    else:
        result.append(num)
print(result)

for i in range(count):
    result.append(0)

print(result)
