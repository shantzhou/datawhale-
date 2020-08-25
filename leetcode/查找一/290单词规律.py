def danci(s,t):
    if not s:
        return False

    t = t.split()
    dit = {}
    for i in range(len(s)):
        if s[i] not in dit:
            if t[i] in dit.values():
                return False
            dit[s[i]] = t[i]
        else:
            if dit[s[i]] != t[i]:
                return False
    return True

def wordPattern(self, pattern, str):
    str = str.split()
    return list(map(pattern.index, pattern)) == list(map(str.index, str))
if __name__ =='__main__':
    pattern = "abba"
    strs = "dog cat cat dog"

    k = danci(pattern,strs)
    print(k)