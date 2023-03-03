n = input("enter the word");
new = ""
for i in range(len(n)):
    if n[i] == 'a':
        new+='$'
    else:
        new+=n[i]   
print(new)
