def num_primorial(n):
    def prime(i, primes):
        for prime in primes:
            if not (i == prime or i % prime):
                return False
        primes.add(i)
        return i

    def primelist(n):
        primes = set([2])
        i, p = 2, 0
        while True:
            if prime(i, primes):
                p += 1
                if p == n:
                    return primes
            i += 1
    lst = primelist(n)
    m = 1
    for x in lst:
        m *= x
    return m
