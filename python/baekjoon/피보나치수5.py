def fibo(n, arr):
    if n == 0:
        return arr[0]
    elif n == 1:
        return arr[1]
    elif arr[n] != 0:
        return arr[n]
    else:
        arr[n] = fibo(n-1, arr) + fibo(n-2, arr)
        print(arr[n])
    
    return arr[n]
    
n = int(input())

if n > 0:
    arr = [0] * (n + 1)
    arr[0] = 0
    arr[1] = 1
    
    print(fibo(n, arr))
else:
    print(n)