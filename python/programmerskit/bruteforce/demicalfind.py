# 프로그래머스 완전 탐색 2단계 소수 찾기
# 못풀어서 정답 봄...

from itertools import permutations

def solution(numbers):
    answer = 0
    insert = 0
    
    numbers = list(numbers)
    numbers.sort()
    print(numbers)
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
            
    for i in list_permute:
        count = 2
        while count * count <= i:
            if i % count == 0:
                count = 0
                break
            count += 1
        if count != 0:
            answer += 1
                    
    print(answer)
    return answer

numbers = "7843"
solution(numbers)

# "17", 3
# "011", 2