import sys

n = list(map(int, sys.stdin.readline().split()))
num = n.copy()

def gcd(n, result):
    for i in range(2, min(n)+1):
        if n[0] % i == 0 and n[1] % i == 0:
            n[0] //= i
            n[1] //= i
            result = gcd(n, result * i)
            
    return result
        
if sum(n) < 2:
    gcdValue = 0
    lcmValue = 0
else:
    gcdValue = gcd(n, 1)
    lcmValue = num[0] * num[1] // gcdValue
    
print(gcdValue)
print(lcmValue)