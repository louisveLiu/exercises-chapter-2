def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for k in range(2, n-1):
        if n % k == 0:
            return False
    else:
        return True
