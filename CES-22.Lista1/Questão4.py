import math


def is_prime(n):
    if n <= 1:
        print("Sem Significado")
        return False
    upper_limit = int(math.sqrt(n))+1
    for i in range(2, upper_limit):
        if n % i == 0:
            return False
    return True


# Example

result = is_prime(997)
if result:
    print("Primo")
else:
    print("Não Primo")
