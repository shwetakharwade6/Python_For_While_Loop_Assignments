a=int(input('enter the no:'))
count=0
while a>0:
    rem=a%10
    count+=1
    a=a//10
print(count)
