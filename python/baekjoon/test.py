arrayA = [12,25,36,20,30,8,42]
# 앞에서 배운 2개의 검색 알고리즘(선형 탐색, 이진 탐색)은
# 배열의 요소를 데이터 수만큼 준비하면 충분했지만,
# 해시 탐색법은 이와 달리 저장하는 데이터의 1.5~2배를 준비해야 합니다.
arrayB = [0] * 11

# 저장할 요소의 배열을 순회하면서
for i in range(len(arrayA)):
    #저장할 공간(첨자)를 계산
    temp = arrayA[i] % 11;
    # 저장할 공간에 데이터가 있으면
    if arrayB[temp] != 0:
        # 데이터가 없는 공간을 찾을때까지
        while arrayB[temp] != 0:
            # temp를 증가, 하지만 배열의 크기가 11이므로, 
            # 인덱스가 10을 넘으면(배열의 크기를 넘으면 안되기에) 0으로 변경합니다.
            print(temp)
            if temp < len(arrayB)-1:
                temp += 1
            else:
                temp = 0
            print(temp)
        # 데이터가 없는 공간을 찾으면 저장합니다.
        arrayB[temp] = arrayA[i]
    # 저장할 공간에 데이터가 없으면
    else:
        # 데이터가 없는 공간을 찾으면 저장합니다.
        arrayB[temp] = arrayA[i]
print(arrayB)

# 저장한 데이터와 찾을 요소를 Argument로 넣어줍니다.
def findHashData(array, target):
    # 저장할 공간에 데이터가 있어서 +1해준 경우를 제외하고는
    # 첨자 = 저장할데이터 % 저장할 배열의 크기입니다..
    uniqueValue = target % len(array);
    
    # 찾고자 하는 값이 맞을 경우가 나올때까지
    while array[uniqueValue] != target:
        # 결과가 원하는 값이 아니면, (저장할데이터+1) % 저장할 배열의 크기
        uniqueValue = (uniqueValue+1) % len(array)
    return uniqueValue

print(findHashData(arrayB, 42))
# => '저장 위치는 0번째 요소입니다.'