import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
maximum = -1e9
minimum = 1e9

def dfs(depth, res, plus, minus, multiply, divide):
    global maximum, minimum
    
    if depth == len(arr):
        maximum = max(res, maximum)
        minimum = min(res, minimum)
        return
    
    if plus:
        dfs(depth + 1, res + arr[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, res - arr[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, res * arr[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(res / arr[depth]), plus, minus, multiply, divide - 1)
            
dfs(1, arr[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)