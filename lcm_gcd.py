def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a,b):
    return (a * b) // gcd(a, b)
a = int(input("enter first number: "))
b = int(input("enter second number: "))
print("GCD:", gcd(a, b))  # Output: 6
print("LCM:", lcm(a, b))  # Output: 36
