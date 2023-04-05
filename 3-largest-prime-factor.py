import sympy
from collections import defaultdict
num = 600851475143
factor = 2
factors = defaultdict(int)
while num > 1:
    if num % factor == 0:
        factors[factor] += 1
        num /= factor
    else:
        factor = sympy.nextprime(factor)

for key in factors:
    print(f"{key}^{factors[key]}")
print(sympy.prod(key**factors[key] for key in factors))
