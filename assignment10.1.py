import math

def is_prime_number(number):
    if number == 1:
        return False
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True

class PrimeNumberGenerator:
    def __init__(self, start, end=None):
        if end is None:
            self.current = 1
            self.limit = start
        else:
            self.current = start
            self.limit = end

    def __iter__(self):
        self.current -= 1
        return self

    def __next__(self):
        if self.current <= self.limit:
            self.current += 1
            while not is_prime_number(self.current):
                self.current += 1
            if self.current > self.limit:
                raise StopIteration
            else:
                return self.current
        else:
            raise StopIteration

# Usage example
prime_number_iterator = iter(PrimeNumberGenerator(1000, 10000))
for prime_number in prime_number_iterator:
    print(prime_number)