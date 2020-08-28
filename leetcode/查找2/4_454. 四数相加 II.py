
def fourSumCount( A, B, C, D):
    from collections import Counter
    record = Counter()
    for i in range(len(A)):
        for j in range(len(B)):
            record[A[i] +B[j]] += 1
    res = 0
    for a in range(len(C)):
        for b in range(len(D)):
            ta = 0 - C[a] - D[b]
            if record.get(ta) != None:
                res += record[ta]
    return res

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
K = fourSumCount(A,B,C,D)
print(K)