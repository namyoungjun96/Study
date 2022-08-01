import sys

people = 0
answer = 0

for i in range(10):
    m, p = map(int, sys.stdin.readline().split())
    
    people += p
    people -= m
    
    answer = max(answer, people)
    
print(answer)