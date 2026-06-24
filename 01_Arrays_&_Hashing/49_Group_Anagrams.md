---
id: "49"
title: Group Anagrams
difficulty: 🟡 Medium
pattern: Arrays & Hashing
leetcode_url: https://leetcode.com/problems/group-anagrams/description/
status: 🟨 Reviewing
time_complexity: O(n * klogk) - n is number of strings, k is the max length of the string. We iterate n times and sorting O(klogk)
space_complexity: O(n * k)
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

## 🚀 Optimal Solution (Fixed Hash Table)

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