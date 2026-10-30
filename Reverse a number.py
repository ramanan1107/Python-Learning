num = int(input("Enter the number: ")) #149
rev = 0
          #14!=0
while (num != 0):
    last = num%10   #1%10  =  last = 1
    rev = (rev*10)+last    #rev = 94x10 + 1         941
    num = num//10   #num = 1//10 = 0

print("The reversed number is: ",rev)
