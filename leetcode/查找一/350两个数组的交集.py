from collections import Counter
def jiaoji(nums1,nums2):
    if not nums1 or not nums2:
        return None
    nums1 = Counter(nums1)
    res = []
    for i in nums2:
        if nums1[i] > 0:
            res.append(i)
            nums1[i] -= 1
    return res

if __name__ == '__main__':
    nums1 =  [4,9,5]
    nums2 = [9,4,9,8,4]
    k = jiaoji(nums1, nums2)
    print(k)
