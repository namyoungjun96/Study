money = []
sum = 0

for i in range(12):
    money.append(float(input()))
    sum+=money[i]

print(money)

moneyAvg = sum / float(len(money))
moneyAvg = round(moneyAvg, 2)

print(moneyAvg)