# 백준 4673번 셀프 넘버
# 20분

memoization = [False] * 10001

for i in range(1, 10000):
    if memoization[i] == False:
        print(i)
        stack = i
        while i != 0:
            stack += i % 10
            i //= 10
        if stack <= 10000:
            memoization[stack] = True
    else:
        stack = i
        while i != 0:
            stack += i % 10
            i //= 10
        if stack <= 10000:
            memoization[stack] = True