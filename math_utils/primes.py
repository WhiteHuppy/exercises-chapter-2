def isprime(n):
    """Returns True if n is a prime else False"""
    if n == 1:
        return False
    
    max_i = int(n ** 0.5)
    for i in range(2, max_i + 1):
        if n % i == 0:
            return False
    return True
