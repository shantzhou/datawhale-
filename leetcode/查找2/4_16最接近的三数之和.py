import numpy as np
def threeSum(nums,target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2] #先随便指定一个和
    cha = abs(res - target) # 随便指定一个差值
    for i in range(len(nums)):
        l, r = i + 1, len(nums) -1
        while l < r:
            if nums[l] + nums[r] == target -nums[i]: #先判断结束的条件
                return nums[l] +nums[r] +nums [i]
            else:
                if abs(nums[l] +nums[r] +nums [i]- target) < cha: # 更新差值
                    cha = abs(nums[l] +nums[r] +nums [i]- target)
                    res = nums[l] +nums[r] +nums [i]
                if nums[l] + nums[r] < target -nums[i]:  # 如果 三个数字之和小于target 右移
                    l += 1
                else:
                    r -= 1 # 大于taget 左移
    return res



if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    k = threeSum(nums,target)
    print(k)