---
id: "239"
title: Sliding Window Maximum
difficulty: 🔴 Hard
pattern: Sliding Window
leetcode_url: https://leetcode.com/problems/sliding-window-maximum/description/
status: 🟨 Reviewing
time_complexity: O(n * k) - n is size of array, k is size of window
space_complexity: O(n - k + 1) - size of output array
date_created: 2026-07-10
---

## 🎯 Core Intuition
This is a pretty easy problem if we are solving using bruteforce, the difficulty is to solve it better.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        l = 0

        for r in range(k - 1, len(nums)):
            res.append(max(nums[l:r + 1]))
            l += 1
        return res
```

