print("to calculate sum of digits of given number")
n=int(input("enter the number: "))
s=0 
while n>0 :
    s=(n%10)+s
    n=n//10
print(s)