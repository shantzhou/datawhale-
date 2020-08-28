


def threesums(s,left,right,target,res):
    pair = None
    while left < right:
        if s[left] +s[right] == target:
            if (s[left], s[right]) != pair:
                res.append([-target,s[left],s[right]])
            pair = (s[left], s[right])
            left += 1
            right -= 1
        elif s[left] + s[right] >target:
            right -= 1
        else:
            left += 1

def threeSum(self, nums: [int]) -> [[int]]:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        # 因为是排序好的数组，如果最小的都大于0可以直接排除
        if nums[i] > 0: break
        # 排除i的重复值
        if i > 0 and nums[i] == nums[i - 1]: continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]: l += 1
                while l < r and nums[r] == nums[r + 1]: r -= 1
            elif sum < 0:
                l += 1
            else:
                r -= 1
    return res
if __name__ == '__main__':
    s = [-1, 0, 1, 2, -1, -4]
    s = sorted(s)
    res = []
    for i in range(len(s)):
        if i > 0 and s[i] == s[i-1]:
            continue
        threesums(s, i+1, len(s)-1, -s[i], res)
    print(res)





