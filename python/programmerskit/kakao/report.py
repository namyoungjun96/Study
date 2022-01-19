# 프로그래머스 카카오 2022 공채 1단계 신고 결과 받기
# 1시간 10분

def solution(id_list, report, k):
    answer = []
    user_list = {}
    report_list = {}
    klist = []
    
    while report:
        reportResult = report.pop()
        reportResult = reportResult.split()
        
        if reportResult[0] not in user_list:
            user_list[reportResult[0]] = [reportResult[1]]
        elif reportResult[1] in user_list.get(reportResult[0]):
            continue
        else:
            user_list[reportResult[0]] += [reportResult[1]]
            
        if reportResult[1] not in report_list:
            report_list[reportResult[1]] = 1
        else:
            report_list[reportResult[1]] += 1
            
    for i in range(len(id_list)):
        if id_list[i] in report_list and report_list.get(id_list[i]) >= k:
            klist.append(1)
        else:
            klist.append(0)
        answer.append(0)
        
    for i in range(len(id_list)):
        if klist[i] == 1:
            for j in range(len(id_list)):
                if id_list[j] in user_list and id_list[i] in user_list.get(id_list[j]):
                    answer[j] += 1
    
    print(answer)
    return answer

id_list, report, k = ["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2
solution(id_list, report, k)

# id_list	report	k	result
# ["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
# ["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]