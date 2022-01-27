# 프로그래머스 카카오 2019 블라인드 채용 2단계 오픈채팅방
# 20분

def solution(record):
    answer = []
    idList = {}
    
    for i in range(len(record)):
        id = record[i].split()
        
        if id[0] == "Enter":
            idList[id[1]] = id[2]
        elif id[0] == "Change":
            idList[id[1]] = id[2]
    
    for i in range(len(record)):
        id = record[i].split()
        
        if id[0] == "Enter":
            answer.append(idList.get(id[1])+"님이 들어왔습니다.")
        elif id[0] == "Leave":
            answer.append(idList.get(id[1])+"님이 나갔습니다.")
    
    return answer