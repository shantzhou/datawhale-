from collections import Counter
def splits(s):
    i_dict = Counter(s)
    # print(i_dict)
    g = {}
    ans = []
    for i in s:
        a = []
        for k in i:
            a.append(k)
        a.sort()
        a = ''.join(a)
        g[i] = a
    new_dict = {}
    for k, v in g.items():
        new_dict.setdefault(v, []).append(k)
    # print(new_dict)
    for k in new_dict.values():

        ans.append(k)
    # return ans


    for i in s:
        k = set(i)
        print(k)

def groupAnagrams( strs):
    from collections import defaultdict
    strs_dict = defaultdict(list)
    res = []
    for str in strs:
        key = ''.join(sorted(list(str)))
        # print(str.split(','))
        strs_dict[key] += str.split(',')
    print(strs_dict)
    for v in strs_dict.values():
        res.append(v)
    return res

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    from collections import defaultdict
    strs_dict = defaultdict(list)
    for str in strs:
        key = ''.join(sorted(list(str)))
        strs_dict[key] += str.split(',')
    return [v for v in strs_dict.values()]

s = ["eat","tea","tan","ate","nat","bat",'eat']
# k = splits(s)
f = groupAnagrams(s)
print(f)

# print(k)