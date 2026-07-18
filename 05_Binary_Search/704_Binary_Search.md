---
id: "704"
title: Binary Search
difficulty: 🟢 Easy
pattern: Binary Search
leetcode_url: https://leetcode.com/problems/binary-search/description/
status: 🟨 Reviewing
time_complexity: O(logn) - dividing the length by 2 each iteration
space_complexity: O(1) - we do not create anything that requires space
date_created: 2026-07-18
---

## 🎯 Core Intuition
This is the classic approach of searching an element in the sorted array, by dividing this array into two halves and searching in the remaining half.


## 🚀 Optimal Solution

### Python Implementation (Recursion)
#### This solution is O(logn) space
```python
class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        
        m = l + (r - l) // 2
        print(m)
        if nums[m] == target:
            return m
        elif nums[m] > target:
            return self.binary_search(l, m - 1, nums, target)
        else:
            return self.binary_search(m + 1, r, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)
```
## 🚀 Optimal Solution

### Python Implementation (Iterative)
#### This solution is O(1) space - no additional space needed
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1
```
