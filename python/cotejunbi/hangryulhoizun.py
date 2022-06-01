# 코딩테스트 행렬 테두리 회전하기
# 행렬을 오른쪽으로 회전시키는 코드임
# 도저히 못풀어서 일단 복붙
# 참고로 왼쪽 아래서부터 위로 올리면서 오른쪽으로 회전시키는 코드임.
# [[1, 2, 3, 4, 5, 6], 
# [7, 8, 9, 10, 11, 12], 
# [13, 14, 15, 16, 17, 18], 
# [19, 20, 21, 22, 23, 24], 
# [25, 26, 27, 28, 29, 30], 
# [31, 32, 33, 34, 35, 36]]
# tmp에 8을 넣는거임

def solution(rows, columns, queries):
    
    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t += 1

    for x1,y1,x2,y2 in queries:
        tmp = array[x1-1][y1-1]
        mini = tmp

        for k in range(x1-1,x2-1):
            test = array[k+1][y1-1]
            array[k][y1-1] = test
            mini = min(mini, test)

        for k in range(y1-1,y2-1):
            test = array[x2-1][k+1]
            array[x2-1][k] = test
            mini = min(mini, test)

        for k in range(x2-1,x1-1,-1):
            test = array[k-1][y2-1]
            array[k][y2-1] = test
            mini = min(mini, test)

        for k in range(y2-1,y1-1,-1):
            test = array[x1-1][k-1]
            array[x1-1][k] = test
            mini = min(mini, test)

        array[x1-1][y1] = tmp
        answer.append(mini)

    return answer