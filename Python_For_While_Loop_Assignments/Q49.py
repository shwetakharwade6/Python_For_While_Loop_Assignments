while True:
    print("\n1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    ch=int(input("Enter choice: "))

    if ch==5:
        break

    a=int(input("Enter a: "))
    b=int(input("Enter b: "))

    if ch==1:
        print(a+b)
    elif ch==2:
        print(a-b)
    elif ch==3:
        print(a*b)
    elif ch==4:
        print(a/b)
    else:
        print("Invalid choice")