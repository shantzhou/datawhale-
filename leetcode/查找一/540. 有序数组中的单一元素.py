def singemo(s):
    if not s:
        return None
    has = {}
    for i in s:
        if i in has:
            has[i] += 1
        else:
            has[i] = 1
    ans = sorted(has.items(), key= lambda x:x[1])
    return ans[0][0]


if __name__ == "__main__":
    s = [1,1,2,3,3,4,4,8,8]
    singemo(s)