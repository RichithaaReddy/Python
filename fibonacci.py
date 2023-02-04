# o/p = 0 1 1 2 3 5 8 13

n = int(input("enter num of series to be printed"))
a,b = 0,1
count = 0

if n <= 0:
   print(a)

elif n == 1:
    print(b)

else:
    while count < n:
     print(a)  # 0 1 1 2 3 5    
     c = int(a)+int(b)
     a=b  
     b=c 
     count += 1
    