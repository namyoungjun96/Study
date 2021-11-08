def recusive(m, n, gcd):
    print(gcd)
    for i in range(2, m):
        if m%i==0 and n%i==0:
            return recusive(m//i, n//i, gcd*i)
        
recusive(60, 48, 1)

### 보류