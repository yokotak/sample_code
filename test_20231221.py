cp = [j for i in range(2, 8) for j in range(i, 50, i)]
print(cp)
primes = [x for x in range(2, 50) if x not in cp]
print (primes)