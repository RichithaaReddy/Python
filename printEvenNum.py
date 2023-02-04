#to print even num in given range
n = int(input("enter the range: "))
if n == 0 or n == 1:
    print("no even num ")
for i in range(2,n):
    if i%2 == 0:
      print(i)
