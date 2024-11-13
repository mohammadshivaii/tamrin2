def sum_digits(x):
    return sum(int(d) for d in str(x))

def sum_prime_factors(x):
    total, factor = 0, 2
    while x > 1:
        while x % factor == 0:
            total += factor
            x //= factor
        factor += 1
    return total

def D(x):
    return x + sum_digits(x) + sum_prime_factors(x)

t = int(input())
numbers = [int(input()) for _ in range(t)]

for number in numbers:
    found = False
    for i in range(4, number):
        if D(i) == number:
            found = True
            break
    print("Yes" if found else "No")
