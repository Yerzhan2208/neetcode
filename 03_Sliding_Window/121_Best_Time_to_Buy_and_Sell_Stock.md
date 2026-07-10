---
id: "121"
title: Best Time to Buy and Sell Stock
difficulty: 🟢 Easy
pattern: Dynamic Programming
leetcode_url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
status: 🟩 Mastered
time_complexity: O(n) - length of array
space_complexity: O(1) - we do not create anything that requires space
date_created: 2026-07-06
---

## 🎯 Core Intuition
I was thinking that we just need to compare two prices, save the lowest one and wait for largest to calculate the maximum profit


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        c = 0
        for i, p in enumerate(prices):
            if i == 0:
                c = p
                continue
            if p <= c:
                c = p
                continue
            maxP = max(maxP, p - c)
        return maxP