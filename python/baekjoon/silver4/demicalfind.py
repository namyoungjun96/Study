# n = int(input())
# numeric = list(map(int, input().split()))
# demical = [True] * 1001
# answer = 0

# m = int(1001 ** 0.5)

# for i in range(2, m + 1):
#     if demical[i] == True:           # i가 소수인 경우 
#         for j in range(i+i, 1001, i): # i이후 i의 배수들을 False 판정
#             demical[j] = False

# for i in range(len(numeric)):
#     if demical[numeric[i]] == True and numeric[i] >= 2:
#         print(numeric[i], demical[numeric[i]])
#         answer += 1

# print(answer)

# 백준 1978번 소수 찾기
# 에라토스테네스의 체로 하니까 안되고 왜 그냥 하니까 되는건지..?
# 1000이하여도 에라토스테네스의 체가 더 빨라서 맞지않나...

n = int(input())
numeric = list(map(int, input().split()))
numeric.sort()
answer = 0

for i in range(len(numeric)):
    count = 0
    for j in range(2, numeric[i]+1):
        if numeric[i] % j == 0:
            count += 1
        
    if count == 1:
        answer += 1

print(answer)