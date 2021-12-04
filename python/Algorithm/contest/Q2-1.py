from collections import deque

string = input()
string = list(string)
queue = deque([])
output = ''
sum = 1

for i in range(len(string)):
    queue.append(string[i])

while queue:
    temp = queue.popleft()
    if not queue:
        sum +=1
        output += str(sum)
        output += temp
    elif temp == queue[0]:
        sum += 1
    elif temp != queue[0] and sum > 1:
        output += str(sum)
        output += temp
        sum = 1
    else:
        output += temp
        
print(output)