def solution(nums):
    answer = -1
    answer += 1
    
    nums.sort()
    n = nums[-1] + nums[-2] + nums[-3] + 1
    demical = [True] * (n)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if demical[i] == True:
            for j in range(i+i, n, i):
                demical[j] = False
    
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if demical[nums[i] + nums[j] + nums[k]]:
                    answer += 1

    print(answer)
    return answer

nums = [1,2,3,4]
solution(nums)