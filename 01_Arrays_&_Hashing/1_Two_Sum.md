---
id: "1"
title: Two Sum
difficulty: 🟢 Easy
pattern: Hash Map
leetcode_url: https://leetcode.com/problems/two-sum/description/
status: 🟨 Reviewing
time_complexity: O(n) - iterations can go all over the nums array
space_complexity: O(n) - Hash Map size depends on the nums length
date_created: 2026-06-23
---

## 🎯 Core Intuition
The tricky part was storing the indices of nums values as the dictionary values, not keys. Therefore, later it is easier to use these indices for the output of the problem


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return [d[diff], i]
            else:
                d[nums[i]] = i