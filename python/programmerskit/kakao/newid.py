# 프로그래머스 카카오 2021 블라인드 채용 1단계 신규 아이디 추천
# 30분

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = list(new_id)
    new_id.reverse()
    id_temp = []
    
    while new_id:
        temp = new_id.pop()
        if ord(temp) >= 97 and ord(temp) < 123 or temp == '-' or temp == '_' or temp == '.' or ord(temp) >= 48 and ord(temp) <= 57:
            id_temp.append(temp)
            if len(id_temp) > 1 and id_temp[-1] == '.' and id_temp[-2] == '.':
                id_temp.pop()
                
    if len(id_temp) > 0 and id_temp[0] == '.':
        del id_temp[0]
    if len(id_temp) > 0 and id_temp[-1] == '.':
        del id_temp[-1]
        
    if len(id_temp) == 0:
        id_temp.append('a')
    if len(id_temp) >= 16:
        id_temp = id_temp[:15]
    if len(id_temp) <= 2:
        for i in range(len(id_temp), 3):
            id_temp.append(id_temp[-1])
            
    if len(id_temp) > 0 and id_temp[0] == '.':
        del id_temp[0]
    if len(id_temp) > 0 and id_temp[-1] == '.':
        del id_temp[-1]
        
    answer = "".join(id_temp)
    
    return answer