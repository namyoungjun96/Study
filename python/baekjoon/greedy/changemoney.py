# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔

money = [1, 5, 10, 50, 100, 500]
pay = int(input())
pay = 1000 - pay
answer = 0

while money:
    temp = money.pop()
    
    if pay >= temp:
        num = pay // temp
        pay -= temp * num
        answer += num

print(answer)