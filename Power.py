base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
res = 1
for i in range(exp):
    res = res*base

print(res)
