a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = int(input("enter the value of c: "))
d = b*b - 4*a*c
if d<0:
    print("roots are imaginary");
else:
    r1 = (-b+d)/2*a
    r2 = (-b-d)/2*a
    print("root 1 = ",r1,"root 2 = ",r2)
