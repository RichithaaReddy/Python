n = int(input("enter number"))
temp = n
sum = 0
while temp > 0:
    digit = temp%10
    sum += digit
    temp //= 10

print(sum)
