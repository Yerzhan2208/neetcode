---
id: "74"
title: Search a 2D Matrix
difficulty: 🟡 Medium
pattern: Binary Search
leetcode_url: https://leetcode.com/problems/search-a-2d-matrix/description/
status: 🟨 Reviewing
time_complexity: O(logn + logm) - n is rows, m is columns
space_complexity: O(1) - we do not create anything that requires space
date_created: 2026-07-18
---

## 🎯 Core Intuition
My first thought was to do the same as for the binary search (iterative approach), but first to find the necessary row, then to search the target in the row. The other approach (one-pass) is more optimal in terms of performance, where we can treat a matrix just as a 1-D array and perform binary search on this array.

## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                return self.searchRow(matrix[m], target)

        return False

    
    def searchRow(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return True
        return False
```