def jiaoji(nums1,nums2):
    if not nums1 or not nums2:
        return None
    nums1 = set(nums1)
    k = []
    for i in nums2:
        # print(i)
        if i in nums1:
            k.append(i)
    k = set(k)

    return k

if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    k = jiaoji(nums1,nums2)
    print(k)