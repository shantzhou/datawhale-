from collections import Counter
s = "anagram"
t = "nagaram"
if len(s) != len(t):
    print("false")

source = Counter(s)
target = Counter(t)
a = 0
if source == target:
    print('true')


