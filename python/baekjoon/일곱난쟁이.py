dwarf = [int(input()) for i in range(9)]
answer = sum(dwarf)
length = len(dwarf)

for i in range(length):
    for j in range(i+1, length):
        if 100 == answer - (dwarf[i] + dwarf[j]):
            num1, num2 = dwarf[i], dwarf[j]
            
            dwarf.remove(num1)
            dwarf.remove(num2)
            dwarf.sort()
            break
    if len(dwarf) < 9:
        break
        
print(dwarf)