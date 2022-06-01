from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    employment = defaultdict(list)
    
    employment = makeEmployment(info, employment)
    
    for key in employment.keys():
        employment[key].sort()
        
    count = 0
    
    for i in query:
        condition = {}
        
        temp = i.split(' ')
        condition = makeCondition(temp, condition, employment)
        
        if len(condition) > 0:
            left, right = 0, len(condition)
            
            while left < right:
                mid = (left + right) // 2
                if condition[mid] >= int(temp[-1]):
                    right = mid
                else:
                    left = mid + 1
            answer.append(len(condition) - left)
            count += 1
            print(count, "번", len(condition), left)
        else:
            answer.append(0)
            count += 1
            print(count, "번")
    
    print(answer)       
    return answer

def makeEmployment(values, dictionary):
    for value in values:
        temp = value.split(' ')
        key = temp[0:-1]
        score = int(temp[-1])
        
        for i in range(len(values)):
            combine = list(combinations(key, i))
            for j in combine:
                temp_key = ''.join(j)
                dictionary[temp_key].append(score)
                
    print(dictionary)
    return dictionary

def makeCondition(value, dictionary, key):
    temp_key = value[:-1]
        
    for j in range(3):
        temp_key.remove('and')
            
    while '-' in temp_key:
        temp_key.remove('-')
    temp_key = ''.join(temp_key)
        
    if temp_key in key:
        dictionary = key[temp_key]
        print(dictionary)
        
    return dictionary
    
    
solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150","- and - and - and chicken 100", "- and - and - and - 150"])