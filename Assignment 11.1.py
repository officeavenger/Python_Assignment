import time

class ExecutionTimer:
    def __enter__(self):
        self.start_time = time.time()
        return self  

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time

def generate_primes_in_range(start, end):
    prime_numbers = []
    for number in range(start, end + 1):
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    divisor = 5
    while divisor * divisor <= number:
        if number % divisor == 0 or number % (divisor + 2) == 0:
            return False
        divisor += 6
    return True

with ExecutionTimer() as timer:
    primes = generate_primes_in_range(2, 50000)

print('Total prime numbers found:', len(primes))
print('Time taken for execution:', timer.elapsed_time, 'seconds')