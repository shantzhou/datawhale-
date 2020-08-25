def splitArray(nums, m):
    def group(mid):
        sums, cnt = 0, 1
        for i in nums:
            if sums + i > mid:
                cnt += 1
                sums = i
            else:
                sums += i
        return cnt

    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if group(mid) <= m:
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    k = splitArray(nums, m)
    print(k)
