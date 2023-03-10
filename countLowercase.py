n = input("enter the word to count characters")
count = 0
for i in n:
    if ( 'a'<=i and i <= 'z' ):
        count += 1
print(count)
