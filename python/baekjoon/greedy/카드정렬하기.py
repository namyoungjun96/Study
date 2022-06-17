import heapq

n = int(input())
card = []
cardtemp = []
answer = 0

for i in range(n):
    heapq.heappush(card, int(input()))

if len(card) <= 1:
    print(0)
else:
    while len(card) > 2:
        temp = heapq.heappop(card)
        temp2 = heapq.heappop(card)
        heapq.heappush(card, (temp + temp2))
        answer += temp + temp2
        
    answer += sum(card)
    print(answer)