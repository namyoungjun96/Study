## 프로그래머스 2020 블라인드 채용 2단계 문자열 압축
## 직접 풀어보지 못하고, 코드를 보았으니 다음에 다시 풀어볼것.
## 이해는 어느정도 한 편이지만 문제를 푸는 방식을 다시 생각해서 풀어봐야함
# 이게 자르면서 어차피 홀수면 홀수대로 처리하는 코드임

def solution(s):
    answer = 10000
    for n in range(1, len(s)//2+2):
        res = ''
        cnt = 1
        tmp = s[:n]
        print("tmp,", tmp, "n,", n)
        
        for i in range(n, len(s) + n, n):
            print(i)
            if tmp == s[i : i+n]:
                print("tmp,", tmp, "s[i:i+n],", s[i : i+n], n)
                cnt += 1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt) + tmp
                print("tmp, ", tmp, "res,", res)
                tmp = s[i : i+n]
                cnt = 1
        
        answer = min(answer, len(res))
        print("answer is ", answer)
        
    print(answer)
    return answer

s = "abcabcabcabcdededededede"
solution(s)