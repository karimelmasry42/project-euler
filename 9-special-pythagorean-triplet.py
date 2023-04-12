"""
12 Apr 2023
https://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
c = 5
while True:
    found = False
    for a in range(1, c):
        for b in range(a, c):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                found = True
                break
        if found:
            break
    if found:
        break
    c += 1
print(f"a = {a}, b = {b}, c = {c}")
print(f"a^2 + b^2 = {a**2 + b**2}, c^2 = {c**2}")
print(f"a+b+c = {a+b+c}, abc = {a*b*c}")
