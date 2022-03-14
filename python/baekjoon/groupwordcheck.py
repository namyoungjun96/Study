# 백준 1316번 그룹 단어 체커
# 20분

n = int(input())
word = list()
answer = 0
for i in range(n):
    word.append(input())
    stack = list()
    fail = 0
    
    for j in range(len(word[i])):
        if word[i][j] not in stack:
            stack.append(word[i][j])
        
        if word[i][j] in stack and stack[len(stack)-1] != word[i][j]:
            fail += 1
    
    if fail == 0:
        answer += 1
        
print(answer)