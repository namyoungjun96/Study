def recusive(num):
    if num!=0:
        recusive(num//2)
        print(num%2, end="")
    else:
        return

recusive(27)