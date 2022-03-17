# 백준 1065번 한수
# 직접 못풀음. 다음에 다시 풀어보기. 생각이 너무 짧은거같다.

n = int(input())

hansoo = 0

for i in range(1, n+1):
    numeric = list(map(int , str(i)))
    if i < 100:
        hansoo += 1
    elif numeric[0] - numeric[1] == numeric[1] - numeric[2]:
        hansoo += 1

print(hansoo)