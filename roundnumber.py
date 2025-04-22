def sum_of_squares(n):
    return sum(int(i) * int(i) for i in str(n))

n = int(input("enter any number"))

if n < 1:
    print("not a positive integer")
elif n == 1:
    print("round number")
else:
    result = sum_of_squares(n)
    while result != 1 :
        result = sum_of_squares(result)
    if result == 1:
        print("round number")
    else:
        print("not a round number")