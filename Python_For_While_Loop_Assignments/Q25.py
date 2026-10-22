s=input("Enter string: ")
c=0

for i in s:
    if i.isalpha() and i not in "aeiouAEIOU":
        c=c+1

print(c)