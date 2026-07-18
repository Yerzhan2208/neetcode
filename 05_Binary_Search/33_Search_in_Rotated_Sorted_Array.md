---
id: "33"
title: Search in Rotated Sorted Array
difficulty: 🟡 Medium
pattern: Binary Search
leetcode_url: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
status: 🟨 Reviewing
time_complexity: O(logn) - dividing the length by 2 each iteration
space_complexity: O(1) - we do not create anything that requires space
date_created: 2026-07-18
---

## 🎯 Core Intuition
This problem is similar to finding the minimum in such an array, however we do not need to compare minimums. In this problem, we need to identify the logic when to change left pointer or right pointer. Here is if we have array `[3, 4, 5, 0, 1, 2]`, mid is 5 and 3 < 5. Then, we can notice that if the target number is either higher than the mid one, or it is lower than the left number, we can then consider second half only. In other cases, we consider the first half.

If we have array `[5, 4, 0, 1, 2, 3]`, mid is 0 and 5 > 0. Then, we can use the symmetric strategy to the first half. If the target is lower than mid, or higher than the right number, then we consider the first half. Otherwise, the second half.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            print(nums[m])
            if target == nums[m]:
                return m
            
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # 5 6 0 1 2 3 4
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
    
        return -1