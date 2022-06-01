def solution(s):
    answer = 0
    left = ['[', '(', '{']
    right = [']', ')', '}']
    temp = s
    stack = []
    
    if len(s)%2 == 0:
        for i in range(len(s)):
            count = 0
            for j in range(len(s)):
                if temp[j] in left:
                    stack.append(temp[j])
                else:
                    if stack and right[left.index(stack[len(stack)-1])] == temp[j]:
                        stack.pop()
                        count += 1
                    else:
                        count = 0
                        break
                    
            if count : answer += 1
            temp = temp[1:] + temp[0]
            stack = list()
    else:
        return 0
                            
    return answer

solution("[](){}")

# s	result
# "[](){}"	3
# "}]()[{"	2
# "[)(]"	0
# "}}}"	0