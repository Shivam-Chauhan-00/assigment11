print("to count the digits in a given number")
n=int(input("enter the number: "))
c=0
while n>0 :
    if n>0 :
        c=c+1
    n=n//10
print(c)