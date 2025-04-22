n = int(input("enter the number of rows to be printed: "))
num = 1
for i in range(1, n+ 1):
    temp = []
    for j in range(i):
        temp.append(num)
        num = num+1
    if i % 2 == 0:
        temp.reverse()
    print(" * ".join(str(n) for n in temp))
    """r=rows"""