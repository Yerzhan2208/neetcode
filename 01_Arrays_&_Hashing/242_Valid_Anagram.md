---
id: "242"
title: Valid Anagram
difficulty: 🟢 Easy
pattern: Hash Map
leetcode_url: https://leetcode.com/problems/valid-anagram/description/
status: 🟩 Mastered
time_complexity: O(n+m) - lenght of s or t
space_complexity: O(1) - hash map of english letters (26 only)
date_created: 2026-06-22
---

## 🎯 Core Intuition
Didn't know about the .get method of dictionary, which can return 0. The idea was the same as optimal solution, but I could not find a way to implement it.

## 🚀 My Solution

### Python Implementation
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res1 = list(s)
        res2 = list(t)
        return sorted(res1) == sorted(res2)
```

## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT