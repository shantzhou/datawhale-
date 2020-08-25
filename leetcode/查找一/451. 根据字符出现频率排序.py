def sortstr(s):
    if not s:
        return s
    has = {}
    for i in s:
        if i in has:
            has[i] +=1
        else:
            has[i] = 1
    ans = []
    has= sorted(has.items(), key=lambda x: x[1], reverse=True)
    for k,v in has:
        for i in range(v):
            ans.append(k)
    ans= ''.join(ans)
    return ans

def frequencySort(s):
    from collections import Counter
    s_dict = Counter(s)
    # sorted返回的是列表元组
    s = sorted(s_dict.items(), key=lambda item: item[1], reverse=True)
    # 因为返回的是字符串
    res = ''
    for key, value in s:
        res += key * value
    return res

if __name__ == "__main__":
    s = 'tree'
    sortstr(s)
