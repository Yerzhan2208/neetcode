---
id: "42"
title: Trapping Rain Water
difficulty: 🔴 Hard
pattern: Two Pointers
leetcode_url: https://leetcode.com/problems/trapping-rain-water/description/
status: 🟩 Mastered
time_complexity: O(n) - the length of the given array
space_complexity: O(1) - we do not create anything that requires space
date_created: 2026-07-05
---

## 🎯 Core Intuition
For each height, we will save the maximum one and subtract the current height from the maximum, so each water section would be within the range. If the height is smaller than the max height, we subtract and get the resulting water, if the height is larger, we change the max height. We do the same for the right side to ensure that water would not leak from the right side and will be limited by the wall


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            leftH = height[l]
            rightH = height[r]
            if leftH <= rightH:
                maxL = max(maxL, leftH)
                res += maxL - leftH
                l += 1
            else:
                maxR = max(maxR, rightH)
                res += maxR - rightH
                r -= 1
        return res