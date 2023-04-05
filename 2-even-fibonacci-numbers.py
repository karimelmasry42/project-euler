i = 2
prev = 1
sum_fib = 0
while i <= 4000000:
    sum_fib += i
    for _ in range(3):
        i, prev = i+prev, i

print(sum_fib)
