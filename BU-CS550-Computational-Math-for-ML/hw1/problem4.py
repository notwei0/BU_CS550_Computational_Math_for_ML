#Problem 4

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def can_be_written(n):
    k = 0
    while 2 * k * k < n: 
        difference = n - 2 * k * k
        if is_prime(difference):
            return True
        k = k + 1
    return False

n = 9
while True:
    if not is_prime(n) and not can_be_written(n):
        print(n)
        break
    n = n + 2
        