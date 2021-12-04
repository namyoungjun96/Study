inputlist = list(map(float, input().split()))                               # 입출력 맞추기위해서 사용했습니다. 일자로 입력하길래...
print(inputlist)
R, M, Y = inputlist[0], inputlist[1], int(inputlist[2])                      # 연이자, 원금, 적립년수

R = (R/100)+1
money = M                               # 불어나는 원금

for i in range(Y):
    money = R*money

print(int(money))