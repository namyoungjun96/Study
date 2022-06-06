form = input()
operator = ['+', '-']
stack = []
count = 0

for i in range(len(form)):
    if form[i] in operator:
        stack.append(int(form[count:i]))
        stack.append(form[i])
        count = i+1
stack.append(int(form[count:]))
stack.reverse()
answer = stack.pop()
minus = 0
count = 0

while stack:
    temp = stack.pop()
    
    if temp == operator[0] and count == 0:
        answer += stack[-1]
    elif count == 0 and temp == operator[1]:
        minus += stack[-1]
        count += 1
    elif count == 1 and temp == operator[0]:
        minus += stack[-1]
    elif temp == operator[1]:
        answer -= minus
        minus = 0
        minus += stack[-1]
        
answer -= minus
print(answer)
        
# 40 - 40 + 50 - 55
# 55 - 50 + 40 - 40 + 30