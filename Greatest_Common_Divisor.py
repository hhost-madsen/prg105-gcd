def gcd(a, b):
    if b == 0:
        return a
    print gcd(b, a % b)

print gcd(20, 10)
print gcd(40, 60)
