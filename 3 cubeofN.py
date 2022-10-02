print("to calcuate the sum of cubes of first N natural numbers")
n=int(input("enter the value of N: "))
m=1
s=0
v=0
while n>=m :
    v=m*m*m
    s=s+v
    m=m+1
print(s)