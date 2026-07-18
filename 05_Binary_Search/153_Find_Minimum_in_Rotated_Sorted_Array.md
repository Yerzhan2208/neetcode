---
id: "153"
title: Find Minimum in Rotated Sorted Array
difficulty: 🟡 Medium
pattern: Binary Search
leetcode_url: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
status: 🟨 Reviewing
time_complexity: O(logn) - dividing the length by 2 each iteration
space_complexity: O(1) - we do not create anything that requires space
date_created: 2026-07-18
---

## 🎯 Core Intuition
This problem does not much differ from the default binary search, so the approach is the same, but differs on the condition if the middle number is higher or equal to the left number, then the minimum should be in the second half, if not, then in the first half.

## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float("infinity")

        while l <= r:
            leftNum = nums[l]
            rightNum = nums[r]

            if leftNum < rightNum:
                res = min(res, nums[l])
                break

            m = l + (r - l) // 2
            mNum = nums[m]

            res = min(mNum, res)
            if mNum >= leftNum:
                l = m + 1
            else:
                r = m - 1
        return res
