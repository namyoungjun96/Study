import time

def fibo(num):
    if num == 1:
        return 1
    if num == 0:
        return 0

    return fibo(num-1) + fibo(num-2)

num=25

start_time = time.time()
res = fibo(num)
end_time = time.time()
spend_time = end_time - start_time
print(res, " time : ", spend_time * 1000, "ms")

print('-----------------------------------------------------------')

memo = [0, 1]

def fibo_memoization(num):
    global memo
    if num >= 2 and len(memo) <= num:
        memo.append(fibo_memoization(num-1) + fibo_memoization(num-2))
    return memo[num]

start_time = time.time()
res = fibo_memoization(num)
end_time = time.time()
spend_time = end_time - start_time
print(res, " time : ", spend_time * 1000, "ms")