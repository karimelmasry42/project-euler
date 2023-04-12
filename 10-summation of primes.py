"""
12 Apr 2023
Karim Ossama Elmasry
https://projecteuler.net/problem=10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from sympy import primerange
print(sum(primerange(2*10**6)))