n=input("enter any password: ")
dg=0
sm=0
up=0
sp=0
if(len(n)>7):
    for i in n:
        if(i.isupper()):
            up=up+1
        elif (i.islower()):
            sm=sm+1
        elif(i.isdigit()):
            dg=dg+1
        else:
            sp=sp+1
    if up >= 1 and sm >= 1 and dg >= 1 and sp >= 1:
        print("Password is strong.")
    else:
        print("Password is weak. Make sure it contains:")
        if up == 0:
            print("- At least one uppercase letter.")
        if sm == 0:
            print("- At least one lowercase letter.")
        if dg == 0:
            print("- At least one digit.")
        if sp == 0:
            print("- At least one special character.")
else:
    print("Password must be at least 8 characters long.")
