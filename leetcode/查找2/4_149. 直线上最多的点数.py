import numpy as np

from collections import defaultdict
from collections import Counter


def maxPoint(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    from collections import Counter, defaultdict
    # 所有点统计
    points_dict = Counter(tuple(point) for point in points)
    # 把唯一点列举出来
    not_repeat_points = list(points_dict.keys())
    n = len(not_repeat_points)
    if n == 1: return points_dict[not_repeat_points[0]]
    res = 0

    # 求最大公约数
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)

    for i in range(n - 1):
        # 点1
        x1, y1 = not_repeat_points[i][0], not_repeat_points[i][1]
        # 斜率
        slope = defaultdict(int)
        for j in range(i + 1, n):
            # 点2
            x2, y2 = not_repeat_points[j][0], not_repeat_points[j][1]
            dy, dx = y2 - y1, x2 - x1
            # 方式一 利用公约数
            g = gcd(dy, dx)
            if g != 0:
                dy //= g
                dx //= g
            slope["{}/{}".format(dy, dx)] += points_dict[not_repeat_points[j]]

        res = max(res, max(slope.values()) + points_dict[not_repeat_points[i]])
    return res


def maxPoints(self,points):
    res = 0
    from collections import defaultdict
    for i in range(len(points)):
        record = defaultdict(int)
        for j in range(len(points)):
            if i != j:
                record[self.get_Slope(points,i,j)] += 1
        for v in record.values():
            res = max(res, v)
    return res + 1

def get_Slope(self,points,i,j):
    return (points[i][0] - points[j][0]) / (points[i][1] - points[j][1])

def maxPointss(points):

    def K(i, j):
        return float('Inf') if i[1] - j[1] == 0 else (i[0] - j[0]) / (i[1] - j[1])

    if len(points) <= 2:
        return len(points)

    maxans = 0
    for i in points:
        same = sum(1 for j in points if j == i)
        # print(same)
        hashmap = Counter([K(i, j) for j in points if j != i])
        tempmax = hashmap.most_common(1)[0][1] if hashmap else 0
        maxans = max(same + tempmax, maxans)

    return maxans


points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
a = maxPoints(points)
print(a)
# print(b)