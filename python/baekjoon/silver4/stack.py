# 백준 10828번 스택
# 20분

n = int(input())
command = []
stack = []

for i in range(n):
    command.append(input())
    
for i in range(n):
    if command[i][:2] == 'pu':
        stack.append(int(command[i][4:]))
    elif command[i][:2] == 'to':
        if stack:
            print(stack[len(stack)-1])
        else:
            print(-1)
    elif command[i][:2] == 'si':
        print(len(stack))
    elif command[i][:2] == 'em':
        if stack:
            print(0)
        else:
            print(1)
    elif command[i][:2] == 'po':
        if stack:
            print(stack.pop())
        else:
            print(-1)