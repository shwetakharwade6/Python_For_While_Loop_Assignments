n=int(input("Enter number: "))
x=n
s=0

while n>0:
    d=n%10
    f=1
    
    for i in range(1,d+1):
        f=f*i
        
    s=s+f
    n=n//10

if x==s:
    print("Strong number")
else:
    print("Not Strong number")