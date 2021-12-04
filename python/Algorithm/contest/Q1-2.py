N = int(input())                # 학생 수 입력
students = []

for i in range(N):
    students.append(int(input()))

rank = sorted(students, reverse=True)
rankdict = {}

for i in range(N):
    if rank[i] in rankdict:
       continue
    else: 
        rankdict[rank[i]] = i+1

for i in range(N):
    print(students[i], rankdict.get(students[i]))