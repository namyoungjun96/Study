# 백준 9012 괄호
# 20분

t = int(input())
answer = []

for i in range(t):
    x = input()
    stack = 0
    
    for j in range(len(x)):
        if x[j] == '(' and stack >= 0:
            stack += 1
        elif x[j] == ')' and stack >= 0:
            stack -= 1
        else:
            stack -= 1
            break
        
    if stack == 0:
        answer.append("YES")
    else:
        answer.append("NO")

for i in range(t):
    print(answer[i])