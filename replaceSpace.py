a = input("enter the string")
new = ""
for i in range(len(a)):
    if a[i] == " ":
        new += "-"
    else:
        new += a[i]
print(new)
