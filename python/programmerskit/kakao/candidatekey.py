# 프로그래머스 카카오 2019 블라인드 채용 2단계 후보키
# 아직 푸는 중 40분째

def solution(relation):
    answer = 0
    answer += 1
    nameMajor = []
    nameClass = []
    majorClass = []
    stop = 0
    
    for i in range(len(relation)):
        for j in range(1, len(relation[i])):
            for k in range(j+1, len(relation[i])):
                if j == 1 and k == 2:
                    nameMajor.append([relation[i][j], relation[i][k]])
                elif j == 1 and k == 3:
                    nameClass.append([relation[i][j], relation[i][k]])
                else:
                    majorClass.append([relation[i][j], relation[i][k]])
                    
    for i in range(len(nameMajor)):
        for j in range(len(nameMajor)):
            if i != j and nameMajor[i][0] == nameMajor[j][0] and nameMajor[i][1] == nameMajor[j][1]:
                stop += 1
    
    if stop == 0:
        answer += 1
    else:
        stop = 0
    
    for i in range(len(nameClass)):
        for j in range(len(nameClass)):
            if i != j and nameClass[i][0] == nameClass[j][0] and nameClass[i][1] == nameClass[j][1]:
                stop += 1
                
    if stop == 0:
        answer += 1
    else:
        stop = 0
        
    for i in range(len(majorClass)):
        for j in range(len(majorClass)):
            if i != j and majorClass[i][0] == majorClass[j][0] and majorClass[i][1] == majorClass[j][1]:
                stop += 1
                
    if stop == 0:
        answer += 1
    else:
        stop = 0
    
    return answer