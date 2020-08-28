def numberOfBoomerangs(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    from collections import Counter
    ans = 0
    for i in points:
        res = Counter()
        for j in points:
            if i != j:
                res[distances(i,j)] += 1
        for k,v in res.items():
            ans += v * (v-1)
    return ans

def distances(point1, point2):
    return ((point1[0] - point2[0]) **2 + (point1[1] -point2[1]) **2)







point = [[0,0],[1,0],[2,0]]
k = numberOfBoomerangs(point)
print(k)