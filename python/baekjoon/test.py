i = 1234
stack = 0

while i != 0:
    print(i)
    stack += i % 10 
    i //= 10

print(i)
print(stack)