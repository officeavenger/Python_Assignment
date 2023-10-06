import time

def performance_monitor(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{fn.__name__} took {elapsed_time:.2f} seconds to complete.")
        return result
    return wrapper

cache = {}

def _cached_(fn):
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = fn(*args, **kwargs)
        cache[args] = result
        return result
    return wrapper

@_cached_
@performance_monitor
def factorial(n):
    fn = 1
    for i in range(1, n + 1):
        time.sleep(0.5)
        fn *= i
    return fn

r1 = factorial(5)  
r2 = factorial(7)  
r3 = factorial(5)  

print(f"Factorial of 5 (cached): {r3}")