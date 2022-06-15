s = int(input())
n = 0
answer = 0

for i in range(1, s+1):
    if n+i <= s:
        n += i
    else:
        print("answer", n, i)
        answer = i-1
        break

if answer == 0:
    answer = i
    
print(answer)