target = 21
m_list = [ 30, 94, 27, 92, 21, 3, 37, 25, 47, 53, 98, 19, 32, 7 ]
print(m_list)
length = len(m_list)
m_list.sort()
print(m_list)

left=0
right=length-1

while left <= right:
    mid = ( right + left ) // 2
    if m_list[mid] == target:
        print(mid+1)
        break
    elif m_list[mid] > target:
        right = mid-1
    else:
        left = mid+1

print('---------------------------------------------')

def binarySearch(array, target, left, right):
    midIndex = ( left + right ) // 2

    if array[midIndex] == target:
        return midIndex+1
    elif array[midIndex] > target:
        binarySearch(array, target, left, midIndex-1)
    else:
        binarySearch(array, target, midIndex+1, right)

print(binarySearch(m_list, target, left, right))