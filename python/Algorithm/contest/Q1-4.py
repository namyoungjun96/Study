numberDict = {0 : '0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7',
              8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

def notation(n, number):
    if number != 0:
        notation(n, number//n)
        print(numberDict[(number%n)], end="")
        
n=int(input())
m=int(input())

notation(n, m)