---
id: "11"
title: Container With Most Water
difficulty: 🟡 Medium
pattern: Two Pointers
leetcode_url: https://leetcode.com/problems/container-with-most-water/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of array
space_complexity: O(1) - we do not create anything that requires space
date_created: 2026-07-04
---

## 🎯 Core Intuition
We just need to use two pointers and for each pair, calculate the area of water it can contain and save the maximum one, then if left height is lower than right height, just move up the left pointer, if the right is lower, move down the right pointer, until we consider all the possible containers of water and return the result.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        w = len(heights) - 1
        l = 0
        r = w
        mx = -1
        while l < r:
            lefth = heights[l]
            righth = heights[r]
            h = min(lefth, righth)
            area = h * w
            if area > mx:
                mx = area
            
            if lefth <= righth:
                l += 1
            elif lefth > righth:
                r -= 1
            w -= 1
        return mx