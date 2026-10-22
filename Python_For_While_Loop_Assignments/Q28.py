n=int(input("Enter number: "))
x=n
s=0
p=len(str(n))

while n>0:
    d=n%10
    s=s+d**p
    n=n//10

if x==s:
    print("Armstrong")
else:
    print("Not Armstrong")