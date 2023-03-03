n = input("enter the string")
s = ""
for i in range(len(n)):
    if i%2 == 0:
        s = s + n[i]
print(s)
