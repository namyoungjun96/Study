# 2020 카카오테크 인턴 5번문제

def solution(rc, operations):
    answer = [[]]

    for i in range(len(operations)):
        if operations[i] == "ShiftRow":
            rc = shiftRow(rc)
        else:
            rc = Rotate(rc)
        print(rc)

    answer = rc
    return answer

def shiftRow(rc):
    temp = rc.pop()
    rc.insert(0, temp)

    return rc

def Rotate(rc):
    # rc[len(rc)-1][len(rc[0])-1] ex . 9
    temp = [rc[0][len(rc)-1], rc[len(rc)-1][0]]
    
    for i in range(len(rc)):
        if i == 0:
            for j in range(len(rc[i])-2, -1, -1):
                rc[i][j+1] = rc[i][j]
        elif i == len(rc)-1:
            for j in range(len(rc[i])-1):
                rc[i][j] = rc[i][j+1]

    print("rc ", rc)

    for i in range(len(rc)-2, 0, -1):
        # rc[i+1][len(rc[0][len(rc[0])-1])] = rc[i][rc[0][len(rc[0])-1]]
        rc[i+1][len(rc[0])-1] = rc[i][len(rc[0])-1]
    
    for i in range(len(rc)-1):
        rc[i][0] = rc[i+1][0]

    rc[1][len(rc[0])-1] = temp[0]
    rc[len(rc)-2][0] = temp[1]

    return rc