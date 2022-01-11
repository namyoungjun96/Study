from itertools import permutations

def solution(numbers):
    answer = 0
    insert = 0
    
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
        print(count)
        if count != 0:
            answer += 1
                    
    print(answer)
    return answer

numbers = "011"
solution(numbers)

# "17", 3
# "011", 2