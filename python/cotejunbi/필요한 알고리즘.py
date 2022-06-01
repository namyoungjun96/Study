# 10진법 -> n진법
import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
    
convert(10, 2)
# 이런식으로
    
# 네이티브 10진법 -> n진법
n, k = 10, 2
while n:
    temp = str(n%k) + temp
    n = n//k

# n진법 -> 10진법 int(string, base)
# string으로 들어가야하고, base에 몇진수인지.

from collections import defaultdict
employment = defaultdict(list)
# 기본적으로 (자료형)을 가진 딕셔너리를 만들 수 있다.

# 하루는 1440분. 시간은 05시는 300분, 5시 10분은 310분.

# for문 만들때 제발 문법실수 하지말자. len인지 아니면 그 자체인지. range는 무조건 len