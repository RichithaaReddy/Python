print("ax3+bx2+cx+d  enter coeff of a,b,c,d ")
lis = []
for i in range(0,4):
    lis.append(int(input()))

x = int(input("enter the value of x: "))
sum = 0
for i in range(0,4):
    sum += (lis[i]*(x**(3-i)))

print(sum)    
