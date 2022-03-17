# 백준 2941번 크로아티아 알파벳
# 1시간

word = input()
# croaword = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer = 0
count = 0

while count <= len(word)-1:
    if word[count] == 'c' and count <= len(word)-2:
        if word[count+1] == '=':
            answer += 1
            count += 2
        elif word[count+1] == '-':
            answer += 1
            count += 2
        else:
            count += 1
            answer += 1
    elif word[count] == 'd' and count <= len(word)-2:
        if word[count+1] == '-':
            answer += 1
            count += 2
        elif count <= len(word)-3 and word[count+1] == 'z' and word[count+2] == '=':
            answer += 1
            count += 3
        else:
            count += 1
            answer += 1
    elif (word[count] == 'l' or word[count] == 'n') and count <= len(word)-2:
        if word[count+1] == 'j':
            answer += 1
            count += 2
        else:
            count += 1
            answer += 1
    elif (word[count] == 's' or word[count] == 'z') and count <= len(word)-2:
        if word[count+1] == '=':
            answer += 1
            count += 2
        else:
            count += 1
            answer += 1
    else:
        count += 1
        answer += 1
        
print(answer)