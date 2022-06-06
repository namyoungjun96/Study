time = [300, 60, 10]
answer = [str(0)] * 3
t = int(input())

for i in range(len(time)):
    if t >= time[i]:
        temp = t // time[i]
        answer[i] = str(temp)
        t -= time[i] * temp
answer = " ".join(answer)

if t:
    print(-1)
else:
    print(answer)