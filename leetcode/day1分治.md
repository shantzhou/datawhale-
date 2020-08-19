## 分治

### 思路：

#### step1：

​		确定切分的条件  直到子问题的长度为1，为终止切分的条件

#### step2：

​    	递归，二分法： 将原问题一分为二，左右区间分开，直到两边

长度为一

#### step3：

​		处理子问题，根据需求而定如何处理：

​		如众数： 长度为一的子问题，众数是其本身

​		如：x的n次幂，二分为奇数次和偶数次      奇数次为偶数次结果再乘以底数，偶数次为两个底数相乘               

​		如：连续子数组最大和：分成左右区间，这里注意的是左边计算和要求从右到左，而右边计算需要从左到右，这样最后合并才是题解想要得到的answer。

#### step4：

​	     合并结果，根据题目需求来处理需要怎么合并



[50. Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)：

```python
def pow_n(x, n):
    if n < 0:
        x = 1/x
        n = -n
    ans = 1
    temp = x
    while n > 0:
        if n % 2 == 1:
            ans *= temp
        temp *= temp
        n //= 2
    return ans
```

[53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)

```python
def sumsson(nums):
    if not nums:
        return -1
    if len(nums) ==1:
        return nums[0]
    left = sumsson(nums[:len(nums)//2])
    right = sumsson(nums[len(nums)//2:])
    sum_left = nums[len(nums) //2 -1]
    temp = 0
    for i in range((len(nums)//2-1), -1, -1):
        # a = nums[len(nums) //2]
        temp += nums[i]
        sum_left = max(temp, sum_left)
    sum_right = nums[len(nums) // 2]
    tmp = 0
    for j in range(len(nums) //2, len(nums)):
        tmp += nums[j]
        sum_right = max(tmp, sum_right)

    return max(left, right,sum_left+sum_right)

```

[169. 多数元素](https://leetcode-cn.com/problems/majority-element/)

```python
def majorityElement( nums):
    hashse = {}
    for i in nums:
        if i in hashse:
            hashse[i] += 1
        else:
            hashse[i] = 1
    a= 0
    for j,k in hashse.items():
        if k > a:
            a = k
            b = j
    return b
```

```

```

```python
def majorityElement( nums):
    if len(nums) ==0:
        return None
    if len(nums) == 1:
        return nums[0]
    left = fenzhi(nums[:len(nums)//2])
    right = fenzhi(nums[len(nums) //2:])

    if left == right:
        return left
    if nums.count(left) > nums.count(right):
        return left
    else:
        return right
```
