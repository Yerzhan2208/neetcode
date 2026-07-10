---
id: "125"
title: Valid Palindrome
difficulty: 🟢 Easy
pattern: Two Pointers
leetcode_url: https://leetcode.com/problems/valid-palindrome/description/
status: 🟩 Mastered
time_complexity: O(n) - the length of the given array
space_complexity: O(1) - we do not create anything that requires space
date_created: 2026-07-04
---

## 🎯 Core Intuition
So, the title of this node in roadmap is Two Pointers, so my intuitive solution is to use two pointers to compare symbols from the left and from the right and if they are not alphabetical and numerical, just add or subtract 1 from left or right respectively.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if(s[l] == s[r]):
                l += 1
                r -= 1
                continue
            else:
                return False
        return True