import sys

n, k = map(int, sys.stdin.readline().split())
res = 0

# while n != 1:
#     if n % k != 0:
#         n -= 1
#         res += 1
#     else:
#         n = int(n / k)
#         res += 1
        
while n >= k:
    target = (n // k) * k
    res += n - target
    n = target
    
    print(target, res, n)
    res += 1
    n //= k
        
res += (n - 1)
print(res)