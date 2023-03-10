a = input("enter the word")
num = 0;
char = 0;
for i in a:
    if ( 'a' <= i and i <= 'z' ) or ('A' <= i and i<= 'Z'):
        char +=  1
    elif ('0'<= i and i <='9'):
        num += 1
print("number",num)
print("character",char)
