order = int(input())
answer = 0

while order:
    if order >= 5 and order % 5 == 0:
        answer += 1
        order -= 5
    elif order >= 3:
        answer += 1
        order -= 3
    else:
        answer = -1
        break
        
print(answer)