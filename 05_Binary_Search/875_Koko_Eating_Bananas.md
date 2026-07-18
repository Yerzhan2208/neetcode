---
id: "875"
title: Koko Eating Bananas
difficulty: 🟡 Medium
pattern: Binary Search
leetcode_url: https://leetcode.com/problems/koko-eating-bananas/description/
status: 🟨 Reviewing
time_complexity: O(nlogm) - n is length of the array, m is the max number
space_complexity: O(1) - we do not create anything that requires space
date_created: 2026-07-18
---

## 🎯 Core Intuition
At first, I was thinking of applying the binary search on the array of piles, searching the number of piles that is optimal for k. However, it also needs the array to be sorted, I tried this approach, but there is a difficulty in defining where to stop and if the total time is lower that the mid k. So, the solution is actually simpler, just by performing binary search in terms of k and finding its minimal by calculating total time iterating through the array.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
		
        while l <= r:
            k = (l + r) // 2
            hh = 0
            for p in piles:
                hh += math.ceil(float(p) / k)
            if hh <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res