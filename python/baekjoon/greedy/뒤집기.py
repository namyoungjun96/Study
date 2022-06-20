s = input()
str = s.split("0")

one = 0

for i in str:
    if i:
        one += 1

if s[0] == "1" and s[-1] == "1":
    print(one-1)
else:
    print(one)