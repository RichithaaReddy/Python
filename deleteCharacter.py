n = input("enter any word ")
num = int(input("enter the position of the character to be deleted"))
new = n[0:num-1]+n[num:len(n)]
print(new)

    
