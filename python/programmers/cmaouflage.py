def solution(clothes):
    answer = 0
    spy = {}
    
    for i in range(len(clothes)):
        if clothes[i][1] in spy:
            spy[clothes[i][1]] = spy.get(clothes[i][1])+1
        else:
            spy[clothes[i][1]] = 1
            
    for i in spy.keys():
        if answer < 1:
            answer += (spy.get(i)+1)
        else:
            answer *= (spy.get(i)+1)
            
    answer -= 1    
    print(answer)    
    return answer

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]

solution(clothes)