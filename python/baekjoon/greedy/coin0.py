import sys

num, money = map(int, sys.stdin.readline().split())
coin = []
answer = 0

for i in range(num):
    coin.append(int(sys.stdin.readline()))

while money:
    temp = coin.pop()
    answer += money // temp
    money -= (money//temp) * temp
        
print(answer)