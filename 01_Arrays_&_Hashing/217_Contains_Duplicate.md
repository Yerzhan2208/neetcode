---
id: "217"
title: Contains Duplicate
difficulty: 🟢 Easy
pattern: Hash Set
leetcode_url: https://leetcode.com/problems/contains-duplicate/description/
status: 🟩 Mastered
time_complexity: O(n) - Hash set access, check if its in the set
space_complexity: O(n) - the size of set
date_created: 2026-06-22
---

## 🎯 Core Intuition
The conceptual trick is using the set to save the seen values, then just search for them in this set


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)    
        return False