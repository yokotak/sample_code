def rGcd(m, n):
    if m % n == 0:
        return n
    else:
        print(n, m % n)
        gcd = rGcd(n, m % n)
        return gcd
    
a = rGcd(2002, 1344)
print(a)