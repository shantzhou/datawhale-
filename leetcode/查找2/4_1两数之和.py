import numpy as np
def twosum(s,t):
    if not s:
        return []
    hsh = {}
    for i,j in enumerate(s):
        hsh[j] =i
    for i,j in enumerate(s):
        k = hsh.get(t-j)
        if k is not None and i != k:
            return [i,k]
def suq(nums,target):
    nums = list(enumerate(nums))
    # print((np.array(nums)).shape)
    # print(nums)
    nums.sort(key=lambda x: x[1])
    print(nums)
    i, j = 0, len(nums) - 1
    for k in range(j+1):
        print(nums[k],nums[k][1],nums[k][0])
    while i < j:
        if nums[i][1] + nums[j][1] > target:

            j -= 1
        elif nums[i][1] + nums[j][1] < target:
            i += 1
        else:
            if nums[j][0] < nums[i][0]:
                nums[j], nums[i] = nums[i], nums[j]
            return nums[i][0], nums[j][0]
if __name__ == '__main__':
    s = [3,2,4]
    t = 6
    # k = twosum(s,t)
    g = suq(s,t)
    # print(k)

