m = int(input("enter the number"))
temp=m
count = 0
while temp>0:
    temp=temp//10
    count = count + 1
new = (count*10) +(m%10)
print(new)

    
    
