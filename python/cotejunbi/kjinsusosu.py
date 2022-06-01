# import string
import math

def solution(n, k):
    answer = 0
    temp = ''
    # temp = (convert(n, k)).split('0')
    while n:
        temp = str(n%k) + temp
        n = n//k
    temp = temp.split('0')
        
#     for i in temp:
#         if '' in temp:
#             temp.remove('')
    
#     temp = [int (i) for i in temp]
    
    for i in temp:
        if len(i) == 0:
            continue
        elif int(i) > 1 and isPrime(int(i)):
            answer += 1
            
    return answer

def isPrime(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

# def convert(num, base) :
#     tmp = string.digits+string.ascii_lowercase
#     q, r = divmod(num, base)
#     if q == 0 :
#         return tmp[r] 
#     else :
#         return convert(q, base) + tmp[r]
    
# def isPrime(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * n

#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:           # i가 소수인 경우 
#             for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
#                 sieve[j] = False

#     # 소수 목록 산출
#     return [i for i in range(2, n) if sieve[i] == True]

#     demical = isPrime(max(temp)+1)
    
#     for i in temp:
#         if i in demical:
#             answer += 1
    
# def isPrime(n):
#     count = 0
#     for i in range(2, n+1):
#         if i%n == 0:
#             count += 1
#     if count == 1:
#         return True
#     else:
#         False
        

    # for i in temp:
    #     if isPrime(i):
    #         answer += 1

# print(isPrime(11))
# print(convert(36, 3).split('0'))
print(solution(36, 3))