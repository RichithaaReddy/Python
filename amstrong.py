#program to find given number = amstrong or not

n = int(input("enter num to find id its amstrong or not: "))
temp = n
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3    #to the power 3
    temp //= 10          # temp = temp/10

if sum == n:
    print("is amstrong")
else:
    print("not aamstrong")
