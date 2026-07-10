---
id: "\r567"
title: "\rPermutation in String"
difficulty: 🟡 Medium
pattern: Hash Map & Sliding Window
leetcode_url: https://leetcode.com/problems/permutation-in-string/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of array
space_complexity: O(1) - length of alphabet
date_created: 2026-07-10
---

## 🎯 Core Intuition
As we need to check if first string is the substring of second one, we just can compare character matrix of s1 and the window of s2. Their size should be equal to len(s1), so we construct a matrix for each window, if they are equal, return True, if not, move window and calculate the matrix for next window.

## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n = len(s1)
        l = 0
        r = n - 1
        sl1 = [0] * 26
        for i in range(n):
            sl1[ord(s1[i]) - 97] += 1
        
        sl2 = [0] * 26
        for i in range(n):
            sl2[ord(s2[i]) - 97] += 1
        while r < len(s2):
            if sl2 == sl1:
                return True
            if r == len(s2) - 1:
                break
            sl2[ord(s2[l]) - 97] -= 1
            l += 1
            r += 1
            sl2[ord(s2[r]) - 97] += 1
            print(sl2)
        return False
```