def containsNearbyAlmostDuplicate(nums, k, t):
    if not nums:
        return -1
    from collections import defaultdict
    res = defaultdict(list)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            ans = []
            if diff(nums,i,j) <= t and abs(i-j) <=k:
                ans=[i,j]
                res[diff(nums,i,j)].append(ans)
    if len(res) ==0:
        return False
    else:
        return True

def diff(nums,i,j):
    return abs(nums[i] -nums[j])

def containsNearbyAlmostDuplicate(self, nums, k, t) -> bool:
    record = set()
    for i in range(len(nums)):
        if len(record) != 0:
            rec = list(record)
            find_index = self.lower_bound(rec, nums[i] - t)
            if find_index != -1 and rec[find_index] <= nums[i] + t:
                return True
        record.add(nums[i])
        if len(record) == k + 1:
            record.remove(nums[i - k])
    return False

def lower_bound(self, nums, target):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = int((low + high) / 2)
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low if nums[low] >= target else -1

nums = [1,5,9,1,5,9]
k = 2
t = 3
g = containsNearbyAlmostDuplicate(nums,k,t)
print(g)