---
id: "49"
title: Group Anagrams
difficulty: 🟡 Medium
pattern: Arrays & Hashing
leetcode_url: https://leetcode.com/problems/group-anagrams/description/
status: 🟨 Reviewing
time_complexity: O(N * KlogK) - N is number of strings, K is the max length of the string. We iterate N times and sorting O(KlogK)
space_complexity: O(N * K)
date_created: 2026-06-24
---

## 🎯 Core Intuition
Any two words that are anagrams will become the exact same string if you sort their letters. By sorting each string and using that sorted version as a dictionary key, we can instantly group all matching anagrams together into lists.

## 🚀 My Solution

### Python Implementation
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for s in strs:
            l = ''.join(sorted(list(s)))
            if l in d:
                d[l].append(s)
            else:
                d[l] = [s]

        for i in d:
            res.append(d[i])

        return res
```

## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())