n = list(map(str, input()))
n.sort(reverse=True)

answer = "".join(n)

if int(answer) % 30 == 0:
    print(answer)
else:
    print(-1)