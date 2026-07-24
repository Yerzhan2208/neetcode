---
id: "271"
title: " Encode and Decode Strings"
difficulty: 🟡 Medium
pattern: Arrays & Hashing
leetcode_url: https://leetcode.com/problems/encode-and-decode-strings/description/
status: 🟩 Mastered
time_complexity: O(m+n) - for both encode and decode where m is sum of lengths of strings, n is number of lengths
space_complexity: O(m+n)
date_created: 2026-06-25
---

## 🎯 Core Intuition
The idea was to save all the words, then add a delimiter and add lengths separated by comma. To decode, we need to find the index of delimiter from the right side (rfind), then we can slice each word for each length we parse


## 🚀 My Solution

### Python Implementation
```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        res = ""
        lens = ""
        for i in range(len(strs)):
            res += strs[i]
            if i != 0:
                lens += ","
            lens += str(len(strs[i]))
        return res + ";" + lens
        
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        sep = s.rfind(";")
        words = s[:sep]
        lens = [int(x) for x in s[sep+1:].split(',')]
        res = []
        for i in lens:
            res.append(s[:i])
            s = s[i:]
        return res
```
## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
```
