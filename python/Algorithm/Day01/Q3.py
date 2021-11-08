def recusive(num):
    for i in range(2, num+1):
        if i==num:
            return num
        elif num%i==0:
            print(i, end=" ")
            return recusive(num//i)

print(recusive(60))