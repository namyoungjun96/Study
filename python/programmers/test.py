temp = { 'a' :'100', 'b' :'100' }

tempList = list(temp.keys())
print(tempList)

a = [1]
a.pop()
if a:
    print("hi")
else:
    print('bye')

print(len(a))
print(a%2)

a = [2, 3, 4, 5]
a.append(2)*2
print(a)