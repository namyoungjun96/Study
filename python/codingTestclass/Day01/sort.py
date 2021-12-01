a=[10, 2, 8, 3, 1]
b=sorted(a)
print("a : ", a)
a.sort()
print("a : ", a)
print("b : ", b)
b=sorted(a, reverse=True)
a.sort(reverse=True)
print("reverse a : ", a)
print("reverse b : ", b)

dict1 = {3:"D", 2:"B", 5:"B", 4:"E", 1:"A"}
print(sorted(dict1))
key1 = sorted(dict1)
print(dict1[key1[0]])

students = [
    ("서호준", "F", 20211201),
    ("김동영", "A", 20211202),
    ("오명균", "A", 20211203),
    ("남영준", "A", 20151562),
]

print(sorted(students, key=lambda x:x[2]))

### tuple의 값대로 정렬 가능

print(sorted(a, key = lambda x : int(str(a)[0])))