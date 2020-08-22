## DP

#### 思路：

##### step1：确定动态规划状态

- 是否存在状态转移?
- 什么样的状态比较好转移，找到对求解问题最方便的状态转移?

想清楚到底是直接用需要求的，比如长度作为dp保存的变量还是用某个判断问题的状态比如是否是回文子串来作为方便求解的状态。

##### step2：写出状态转移方程

​	以[Leetcode 300.最长上升子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/) 为例，

```
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
```

对于每个子序列，最小的长度为1， 如第0位的10，其dp[0] =1, 对于dp[1],因为9<10,故dp[1] =1,同理dp[2] =1, 到了5， 5 >2,故dp[3] +=1 --->=2, 以此类推，得到一个之前子序列的dp，递推求解即可。

其状态转移方程实现如下 

```python
for i in range(len(nums)):
    for j in range(i):
    	if nums[i]>nums[j]:
    		dp[i]=max(dp[i],dp[j]+1)
```

 在实际问题中，如果不能很快得出这个递推公式，可以先尝试一步一步把前面几步写出来，如果还是不行很可能就是 dp 数组的定义不够恰当，需要回到第一步重新定义 dp 数组的含义；或者可能是 dp 数组存储的信息还不够，不足以推出下一步的答案，需要把 dp 数组扩大成二维数组甚至三维数组。

##### step3：考虑初始条件

 这是决定整个程序能否跑通的重要步骤，当我们确定好状态转移方程，我们就需要考虑一下边界值，边界值考虑主要又分为三个地方

- dp数组整体的初始值
- dp数组(二维)i=0和j=0的地方
- dp存放状态的长度，是整个数组的长度还是数组长度加一，这点需要特别注意。

对于本问题，子序列最少也是自己，所以长度为1，这样我们就可以方便的把所有的`dp`初始化为1，再考虑长度问题，由于`dp[i]`代表的是`nums[i]`的最长子序列长度，所以并不需要加一。 所以用代码表示就是`dp=[1]*len(nums)`

这里额外总结几种Python常用的初始化方法：

- 对于产生一个全为1，长度为n的数组：

  ```python
  1. dp=[1 for _ in range(n)]
  2. dp=[1]*n
  ```

- 对于产生一个全为0，长度为m，宽度为n的二维矩阵：

  ```python
  1. dp=[[0 for _ in range(n)] for _ in range(m)]
  2. dp=[[0]*n for _ in range(m)]
  ```

##### step4：考虑输出的状态

主要有以下三种形式，对于具体问题，我们一定要想清楚到底dp数组里存储的是哪些值，最后我们需要的是数组中的哪些值：

- 返回dp数组中最后一个值作为输出，一般对应二维dp问题。

- 返回dp数组中最大的那个数字，一般对应记录最大值问题。

- 返回保存的最大值，一般是`Maxval=max(Maxval,dp[i])`这样的形式。

  **Tips：**这个公式必须是在满足递增的条件下，也就是`nums[i]>nums[j]`的时候才能成立，并不是`nums[i]`前面所有数字都满足这个条件的，理解好这个条件就很容易懂接下来在输出时候应该是`max(dp)`而不是`dp[-1]`，原因就是dp数组由于计算递增的子序列长度，所以dp数组里中间可能有值会是比最后遍历的数值大的情况，每次遍历`nums[j]`所对应的位置都是比`nums[i]`小的那个数。举个例子，比如`nums=[1,3,6,7,9,4,10,5,6]`,而最后`dp=[1,2,3,4,5,3,6,4,5]`。 总结一下，最后的结果应该返回dp数组中值最大的数。

[Leetcode 300.最长上升子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/) ：

```python
def satra(s):
    if not s: # 临界条件
        return 0
    dp = [1] * len(s)   # dp的长度
    for i in range(len(s)): # 遍历所有s的值i
        for j in range(i): #对i长度前的所有字符j
            if s[i] > s[j]: #如果在长度i里 si的值大于sj的值 则 dp j的值加1
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
if __name__ == '__main__':
    s = [10, 9, 2, 5, 3, 7, 101, 18]
    k = satra(s)
    print(k)

```

###### [Leetcode5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)

```
def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[0]*n for _ in range(n)]  #定义动态规划状态转移矩阵
        for i in range(n):  #   初始化对角线，单个字符子序列就是1
            dp[i][i]=1
        for i in range(n,-1,-1):  #从右下角开始往上遍历
            for j in range(i+1,n):
                if s[i]==s[j]:   #当两个字符相等时，直接子字符串加2
                    dp[i][j]= dp[i+1][j-1]+2  
                else:           #不相等时，取某边最长的字符
                    dp[i][j]=max(dp[i][j-1],dp[i+1][j])
        return dp[0][-1]   #返回右上角位置的状态就是最长
```

```python
def sadasd(s):
    lenth = len(s)
    dp = [[0]*lenth for _ in range(lenth)] # 初始化二维dp数组
    for i in range(lenth):
        dp[i][i] = 1   #对角线
    # print(dp)
    for i in range(lenth,-1,-1):#从右下角开始遍历
        for j in range(i+1,lenth): #
            print(i,j)
            if s[j] ==s[i]:
                dp[i][j] = dp[i+1][j-1] +2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    return dp[0][-1]

if __name__ == '__main__':
    s = 'bbbab'
    k = sadasd(s)
    print(k)
```

##### [Leetcode72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)

```python
def distance(str1,str2):
    n = len(str1)
    m = len(str2)
    dp = [[0]*(m+1) for _ in range(n+1)] #初始化dp  dp存储为各个点的代价
    for i in range(m+1): #插入操作即可
        dp[0][i] = i
    for j in range(n+1):#删除即可
        dp[j][0] = j
    for i in range(1,n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:#最后一个字符相等 那么代价和上一步相同
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) +1 #从各个操作中 找代价最小的操作 
    return dp[-1][-1]

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    k =distance(word1,word2)
    print(k)
```

##### [Leetcode198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)

```python
def findmax(s):
    if not s:
        return 0
    if len(s) ==1:
        return s[0]
    dp = [0 for _ in s]
    if len(s) <=2:

    dp[0] =s[0]
    dp[1] = max(s[0],s[1])
    for i in range(2,len(s)):
        dp[i] = max(dp[i-2] +s[i], dp[i-1])
    return max(dp)

if __name__ == '__main__':
    s = [1,2,3,1]
    k = findmax(s)
    print(k)
```

##### [Leetcode213. 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/)

```python
class Solution(object):
    def rob(self, s):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not s:
            return 0
        if len(s)<3:
            return max(s)
        a=self.findmax(s[1:])
        b=self.findmax(s[:-1])
        return max(a,b)


    def findmax(self,s):
        if len(s) ==1:
            return s[0]
        dp = [0 for _ in s]
        dp[0] =s[0]
        dp[1] = max(s[0],s[1])
        for i in range(2,len(s)):
            dp[i] = max(dp[i-2] +s[i], dp[i-1])
        return max(dp)
```

