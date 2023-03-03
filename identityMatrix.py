m = int(input("enter num of rows and cols"))
l = [] #main list
for i in range(m):
    l1 = [] #creating seperate list 
    for j in range(m):
        if i==j:
            l1.append(1)
        else:
            l1.append(0)
    l.append(l1)

for i in range(m):
    for j in range(m):
        print(l[i][j],end=" ")
    print() # takes new line
            
