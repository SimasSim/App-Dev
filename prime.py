import time


def current_milli_time():
    return round(time.time() * 1000)


def is_prime(x):

    if x % 2 == 0:  # Skip even numbers
        return False
    for i in range(2, int(x**0.5) + 1):  # Only check up to sqrt(x)
        if x % i == 0:
            return False  # If divisible, not a prime
    return True  # If no factors found, it's prime


rs = 1000
re = 40000

start = current_milli_time()
for i in range(rs, re):
    if is_prime(i):
        print(i, "is prime")
end = current_milli_time()

print((re-rs), "numbers searched in", end-start, "milliseconds")