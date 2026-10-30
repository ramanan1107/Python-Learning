num = 87928
org = num
digit = 0
last = 0
rev = 0
while(num != 0):
    last = num%10
            #0  x 10 + 9 = 9
            #9 x 10 + 8 = 98
            #98x10 + 4 = 984
    rev =  rev * 10 + last
    digit = digit+1
    num = num//10  #48

if org == rev:
    print("Plaindrome")
else:
    print("Not Plaindrome")

    
    
