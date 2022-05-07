# 2020 카카오테크 인턴 2번문제

def solution(rc, operations):
    answer = [[]]

    Rotate(rc)
    return answer

def shiftRow(rc):
    temp = rc.pop()
    rc.insert(0, temp)

    return rc

def Rotate(rc):
    temp = [rc[0][len(rc)-1], rc[len(rc)-1][len(rc[0])-1], rc[len(rc)-1][0]]
    print(temp)
    
    for i in range(len(rc)):
        if i == 0:
            for j in range(len(rc)-2, 0, -1):
                rc[i][j+1] = rc[i][j]
        elif i == len(rc)-1:
            for j in range(len(rc)-2, 0, -1):
                rc[i][j+1] = rc[i][j]

    for i in range(len(rc)-2, 0, -1):
        rc[i+1][rc[0][len(rc[0])-1]] = rc[i][rc[0][len(rc[0])-1]]
    
    for i in range(len(rc)-1):
        rc[i][0] = rc[i+1][0]
        
solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"])