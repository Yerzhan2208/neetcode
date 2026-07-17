---
id: "739"
title: Daily Temperatures
difficulty: 🟡 Medium
pattern: Stack & Dynamic Programming
leetcode_url: https://leetcode.com/problems/daily-temperatures/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of array
space_complexity: O(n) - the length of the given array
date_created: 2026-07-17
---

## 🎯 Core Intuition
The solution is tricky because I struggle to save the results for numbers before the current index as I thought solution should be using stacks only, however, in related topics I have noticed just array. Therefore, I started using res array as a counter for each index in temperatures. We use monotonically decreasing stack to track the temperatures, if the current index is not following, we just pop until the sequence to recover and when we pop, we update the counter of the popped element, thus creating a resulting array.

## 🚀 Stack Solution

### Python Implementation
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append((t, i))
        return res
```
