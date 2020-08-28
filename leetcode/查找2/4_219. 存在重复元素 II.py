def containsNear(nums, k):
    if not nums:
        return False
    from collections import defaultdict
    has = defaultdict(list)
    for i,j in enumerate(nums):
        has[j].append(i)
    ans = []
    for v in has.values():
        for i in range(len(v)):
            for j in range(len(v)):
                if i != j:
                    if abs(v[j] -v[i]) <= k:
                        ans.append([i,j])
    if len(ans) ==0:
        return  False
    else:
        return True
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool: #滑动法
        record = set()
        for i in range(len(nums)):
            if nums[i] in record:
                return True
            record.add(nums[i])
            if len(record) == k+1:
                record.remove(nums[i-k])
        return False

nums = [1,2,3,1]
k = 3
g = containsNearbyDuplicate(nums,k)
print(g)
