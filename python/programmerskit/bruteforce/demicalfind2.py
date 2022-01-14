# 프로그래머스 완전 탐색 2단계 소수 찾기
# 못풀어서 정답 봄...

from itertools import permutations
import math

def solution(numbers):
    answer = 0
    insert = 0
    
    numbers = list(numbers)
    numbers.sort()
    permute = list(permutations(numbers, len(numbers)))
    list_permute = [''.join(map(str, i)) for i in permute]
    for i in range(len(numbers)):
        if int(numbers[i]) > 1:
            list_permute.insert(insert, int(numbers[i]))
            insert += 1
    list_permute = list(map(int, list_permute))
    list_permute = list(set(list_permute))
    list_permute.sort()
    print(list_permute)
    
    array = [True for i in range(max(list_permute) + 1)] 

    for i in range(2, int(math.sqrt(max(list_permute))) + 1): 
        if array[i] == True: 
            j = 2 
            while i * j <= max(list_permute):
                array[i * j] = False
                j += 1
                
    for i in list_permute:
        if array[i] == True:
            answer += 1
    
    print(answer)
    return answer

numbers = "7843"
solution(numbers)

# "17", 3
# "011", 2