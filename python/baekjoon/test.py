def solution(queue1, queue2):
    answer = -2
    if ((sum(queue1) + sum(queue2)) % 2) == 1:
        return -1

    #answer = queueHandler(queue1, queue2)
    answer = recursive(queue1, queue2, 1)
    return answer

def recursive(queue1, queue2, count):
    print(queue1, queue2)
    if sum(queue1) == sum(queue2):
        return count
    elif sum(queue1) > sum(queue2) and count < (len(queue1) + len(queue2)) * 1.5:
        queue2.append(queue1.pop(0))
        return recursive(queue1, queue2, count+1)
    elif sum(queue1) < sum(queue2) and count < (len(queue1) + len(queue2)) * 1.5:
        queue1.append(queue2.pop(0))
        return recursive(queue1, queue2, count+1)
    else:
        return -1
    
def queueHandler(queue1, queue2):
    count = 0

    while sum(queue1) != sum(queue2):
        if sum(queue1) > sum(queue2):
            queue2.append(queue1.pop(0))
        else:
            queue1.append(queue2.pop(0))
        count += 1

        if count > (len(queue1) + len(queue2)) * 2:
            return -1

    return count

# def testSample():
#     assert solution([3, 2, 7, 2], [4, 6, 5, 1]) == 2
#     assert solution([1, 2, 1, 2], [1, 10, 1, 2]) == 7
#     assert solution([1, 1], [1, 5]) == -1
    
#testSample()

print("answer is", solution([1, 2, 1, 2], [1, 10, 1, 2]))
print("answer is", solution([1, 1], [1, 5]))