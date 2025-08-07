def feed(l):
    for i in l:
        yield i
l=['1..100','101..200','201..300']
load=feed(l)        
print(next(load))
print(next(load))

#Example: Simple Generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter=count_up_to(5)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
# Example: Fibonacci Sequence Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
fib_gen = fibonacci(10)
for num in fib_gen:
    print(num, end=' ')  # Output: 0 1 1 2 3 5 8 13 21 34

# Example: Infinite Generator
def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1
infinite_gen = infinite_numbers()
print(next(infinite_gen))  # Output: 1 
print(next(infinite_gen))  # Output: 2
print(next(infinite_gen))  # Output: 3
# Example: Generator for Squares
def squares(n):
    for i in range(n):
        yield i * i
squares_gen = squares(5)
for square in squares_gen:
    print(square, end=' ')  # Output: 0 1 4 9 16
# Example: Generator for Even Numbers
def even_numbers(n):    
    for i in range(0, n, 2):
        yield i
even_gen = even_numbers(10)
for even in even_gen:
    print(even, end=' ')  # Output: 0 2 4 6 8

# Example: Generator for Odd Numbers
def odd_numbers(n):
    for i in range(1, n, 2):
        yield i
odd_gen = odd_numbers(10)
for odd in odd_gen:
    print(odd, end=' ')  # Output: 1 3 5 7 9
# Example: Generator for Prime Numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_numbers(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1
prime_gen = prime_numbers(10)
for prime in prime_gen:
    print(prime, end=' ')  # Output: 2 3 5 7 11 13 17 19 23 29
# Example: Generator for Factorials
def factorials(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact
fact_gen = factorials(5)
for fact in fact_gen:
    print(fact, end=' ')  # Output: 1 2 6 24 120
# Example: Generator for Palindromes
def is_palindrome(s):
    return s == s[::-1]
def palindrome_generator(n):
    count = 0
    num = 0
    while count < n:
        if is_palindrome(str(num)):
            yield num
            count += 1
        num += 1
palindrome_gen = palindrome_generator(10)
for pal in palindrome_gen:
    print(pal, end=' ')  # Output: 0 1 2 3 4 5 6 7 8 9
# Example: Generator for Powers of Two
def powers_of_two(n):
    for i in range(n):
        yield 2 ** i
power_gen = powers_of_two(5)
for power in power_gen:
    print(power, end=' ')  # Output: 1 2 4 8 16
# Example: Generator for Triangular Numbers
def triangular_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
        yield total
triangular_gen = triangular_numbers(5)
for tri in triangular_gen:
    print(tri, end=' ')  # Output: 1 3 6 10 15
# Example: Generator for Arithmetic Progression
def arithmetic_progression(start, step, n):
    for i in range(n):
        yield start + i * step
ap_gen = arithmetic_progression(1, 3, 5)
for ap in ap_gen:
    print(ap, end=' ')  # Output: 1 4 7 10 13
    
