# 내장함수
import builtins

builtins.print()

ranking = {'A' : 100, 'B' : 85, 'C' : 95}

print(sorted(ranking, key=ranking.get, reverse =True))

# 내장 라이브러리
from collections import defaultdict

s = "asdfafdfasdagvhbkhkujoiuwenfoinsaoic"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1

d = defaultdict(int)
for c in s:
    d[c] += 1

print(d)