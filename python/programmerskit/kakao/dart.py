# 프로그래머스 카카오 2018 블라인드 채용 1단계 다트 게임
# 1시간

def solution(dartResult):
    answer = 0
    sum = []
    dartResult = list(dartResult)
    count = -1
    ten = 0
    
    for i in range(len(dartResult)):
        if ord(dartResult[i]) == 49 and ord(dartResult[i+1]) == 48:
            sum.append(10)
            count += 1 
            ten = 1
        elif ord(dartResult[i]) >= 48 and ord(dartResult[i]) <= 57:
            sum.append(int(dartResult[i]))
            count += 1
            if ten == 1:
                count -=1
                sum.pop()
                ten = 0
        elif dartResult[i] == "D":
            sum[count] = sum[count] ** 2
        elif dartResult[i] == "T":
            sum[count] = sum[count] ** 3
        elif dartResult[i] == "*" and count > 0:
            sum[count] *= 2
            sum[count-1] *= 2
        elif dartResult[i] == "*" and count == 0:
            sum[count] *= 2
        elif dartResult[i] == "#":
            sum[count] = -(sum[count])
            
    print(sum)
    for i in range(len(sum)):
        answer += sum[i]
    return answer

dartResult = "1S2D*3T"
solution(dartResult)