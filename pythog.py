#Python Program to Find All Pythagorean Triplets in the Range
h = int(input("enter the upper limit : "))
for i in range(1,h):
    for j in range(i,h):
        sq = i**2 + j**2
        sq = sq**0.5
        n = int(sq)
        if sq-n == 0.0 and sq in range(1,h+1):
            print(i,j,n)
