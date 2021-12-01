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