def is_prime(num):
    import math
    if num == 2:
        return True
    if num % 2 == 0 or num <= 1:
        return False

    sqrt = int(math.sqrt(num)) + 1

    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
        return False
    return True
