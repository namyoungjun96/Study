n = float(10**100)
k = float(10)
print(n)
##n, k = map(float, input().split())
a = [False,False] + [True] * (n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)

num = []

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        if primes[i] * primes[j] == n:
            num.append(primes[i])
            num.append(primes[j])
            break
    if len(num) != 0:
        break
    
if num[0] <= k or num[1] <= k:
    print("BAD", num[0])
else:
    print("GOOD")
    
