# 프로그래머스 카카오 2018 공채 1단계 비밀지도
# 30분

def solution(n, arr1, arr2):
    answer = []
    arr1.reverse()
    arr2.reverse()
    map1 = []
    map2 = []
    mapTemp = []
    
    for i in range(n):
        temp = str(bin(arr1.pop())[2:])
        if len(temp) != n:
            temp = list(temp)
            
            for j in range(len(temp)-1, n-1):
                temp.insert(0, "0")
            temp = ''.join(temp)
        map1.append(temp)
        
        temp = str(bin(arr2.pop())[2:])
        if len(temp) != n:
            temp = list(temp)
            
            for j in range(len(temp)-1, n-1):
                temp.insert(0, "0")
            temp = ''.join(temp)
        map2.append(temp)
        
    for i in range(n):
        mapTemp.append(list(map1[i]))
        
        for j in range(n):
            temp = list(map2[i])
            
            if mapTemp[i][j] == "0" and temp[j] == "1":
                mapTemp[i][j] = "1"
                
    for i in range(n):
        temp = ""
        for j in range(n):
            if mapTemp[i][j] == "1":
                temp += "#"
            elif mapTemp[i][j] == "0":
                temp += " "
                
        answer.append(temp)
    
    return answer