# 프로그래머스 2021 카카오 채용연계형 인턴십 2단계 거리두기 확인하기
# 탐색으로 풀으란 말이란것을 알았지만...
# 걍 .. 하다보니 이렇게 풀었다..


def solution(places):
    answer = [0] * 5
    
    for i in range(len(places)):
        fail = 0
        
        for j in range(len(places)):
            for h in range(len(places)):
                if places[i][j][h] == "P":
                    if j + 1 < len(places) and places[i][j+1][h] == "P":
                        fail += 1
                        break
                    elif j + 1 < len(places) and places[i][j+1][h] == "O":
                        if h + 1 < len(places) and places[i][j+1][h+1] == "P":
                            fail += 1
                            break
                        elif j + 2 < len(places) and places[i][j+2][h] == "P":
                            fail += 1
                            break
                    if h + 1 < len(places) and places[i][j][h+1] == "P":
                        fail += 1
                        break
                    elif h + 1 < len(places) and places[i][j][h+1] == "O":
                        if j - 1 >= 0 and places[i][j-1][h+1] == "P":
                            fail += 1
                            break
                        elif h + 2 < len(places) and places[i][j][h+2] == "P":
                            fail += 1
                            break
                    if j - 1 >= 0 and places[i][j-1][h] == "P":
                        fail += 1
                        break
                    elif j - 1 >= len(places) and places[i][j-1][h] == "O":
                        if h - 1 > 0 and places[i][j-1][h-1] == "P":
                            fail += 1
                            break
                        elif j - 2 < len(places) and places[i][j-2][h] == "P":
                            fail += 1
                            break
                    if h - 1 >= 0 and places[i][j][h-1] == "P":
                        fail += 1
                        break
                    elif h - 2 >= 0 and places[i][j][h-1] == "O":
                        if j + 1 < len(places) and places[i][j+1][h-1] == "P":
                            fail += 1
                            break
                        elif h - 2 < len(places) and places[i][j][h-2] == "P":
                            fail += 1
                            break
                    
        if fail == 0:
            answer[i] = 1
            
    print(answer)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

solution(places)