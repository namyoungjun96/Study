# 괄호 변환
# 내가 넣은거라곤 분리하는것과 체크하는 코드 뿐..
# 나머지는 어태 생갃하냐 시발

def solution(p):
    answer = ''
    # 과정 1
    if p:
        # 과정 2
        u, v = divide(p)
        
        # 과정 3
        if check(u):
            # 과정 3-1
            return u + solution(v)
        # 과정 4
        else:
            # 과정 4-1
            answer = '('
            # 과정 4-2
            answer += solution(v)
            # 과정 4-3
            answer += ')'
            
            # 과정 4-4
            for p in u[1:len(u) - 1]:
                print(answer, u, p, u[1:len(u) - 1])
                if p == '(':
                    answer += ')'
                else:
                    answer += '('
    # 과정 1 빈 문자열
    else:
        return answer
    
    return answer

def divide(p):
    temp = []
    u = p[0]
    v = ''
    for i in range(1, len(p)):
        if u != p[i]:
            u += p[i]
            if u.count('(') == u.count(')'):
                v += p[i+1:]
                break
        else:
            u += p[i]
    return u, v

def check(letter):
    if letter[0] == '(':
        return 1
    else:
        return 0
    
print(solution("()))((()"))

"(()())()"	"(()())()"
")("	"()"
"()))((()"	"()(())()"