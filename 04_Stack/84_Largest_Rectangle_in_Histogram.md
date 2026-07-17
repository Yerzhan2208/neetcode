---
id: "84"
title: Largest Rectangle in Histogram
difficulty: 🔴 Hard
pattern: Stack
leetcode_url: https://leetcode.com/problems/largest-rectangle-in-histogram/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of array
space_complexity: O(n) - length of stack
date_created: 2026-07-18
---

## 🎯 Core Intuition
I was first thinking about the trivial bruteforce solution and it is not hard, just very slow. So, to improve the algorithm, we need to save the leftmost and rightmost lowest height for each of the height to understand how it can be extended. If we use the monotonic increasing stack for left to right and vice-versa, we can identify the index of each lowest left and right height. This way, we can calculate the area for each height that can be extended. To deal with first and last elements, we can fill the leftmost and rightmost arrays with -1 and n respectively, then just increment the leftmost and decrement the rightmost to get the width.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]

            stack.append(i)
        print(leftMost)

        stack = []
        rightMost = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]

            stack.append(i)
        print(rightMost)

        maxArea = 0
        for i in range(n):
            right = rightMost[i] - 1
            left = leftMost[i] + 1
            maxArea = max(maxArea, heights[i] * (right - left + 1))
        return maxArea
