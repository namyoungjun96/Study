import sys

h, w = map(int, sys.stdin.readline().split())
world = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(1, w - 1):
    left_max = max(world[:i])
    right_max = max(world[i+1:])

    compare = min(left_max, right_max)
    print("left_max", left_max, "right_max", right_max, "compare", compare)

    if world[i] < compare:
        ans += compare - world[i]

print(ans)