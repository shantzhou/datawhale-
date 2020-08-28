def threeSum( nums: [int], target) -> [[int]]:
    nums.sort()
    res = []
    if len(nums) < 4:
        return res
    if len(nums) ==4 and sum(nums) == target:
        res.append(nums)
        return res
    for i in range(len(nums) - 3):
        # 因为是排序好的数组，如果最小的都大于0可以直接排除
        # if nums[i] > 0: break
        # 排除i的重复值
        if i > 0 and nums[i] == nums[i - 1]: continue
        for j in range(i+1,len(nums) -2):
            if j > i+1 and nums[j] == nums[j -1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r] +nums[j]
                if sum == target:
                    res.append([nums[i],nums[j], nums[l],  nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif sum < target:
                    l += 1
                else:
                    r -= 1
    return res
if __name__ =='__main__':
    s =   [1, 0, -1, 0, -2, 2]
    target = 0
    k = threeSum(s,target)
    print(k)