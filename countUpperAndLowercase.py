a = input("enter the word")
lower = 0
upper = 0
for i in a:
    if ( 'a'<=i and i <= 'z' ):
        lower += 1
    elif ( 'A'<=i and i <= 'Z' ):
        upper += 1
print("lowercase",lower)
print("upper case",upper)
