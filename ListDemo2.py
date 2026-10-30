list1 = [20,80,90,12,15,70,50]
list2 = [10,15,12,19,80]

for i in list1:
    for j in list2:
        if i==j:
            list2.remove(j)
list3 = list1+list2
print(list3)
