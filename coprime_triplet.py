def coprime(i,j):
    return gcd(i,j)==1
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a=int(input("enter any number: "))

for i in range(5,a):
    for j in range(4,a):
        for k in range(3,a):
            if (k*k + j*j== i*i) and coprime(i,j) and coprime(j,k) and coprime(i,k):
                print(k,j,i)