---
id: "167"
title: Two Sum II - Input Array Is Sorted
difficulty: 🟡 Medium
pattern: Two Pointers
leetcode_url: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of array
space_complexity: O(1) - we do not create anything that requires space
date_created: 2026-07-04
---

## 🎯 Core Intuition
I used two pointers and realized that if the sum of two numbers l and r is larger than target, then we need to move the right pointer down (decrease the sum), otherwise if the sum is lower than the target, we need to move the left pointer up (increase the sum). This way, we get the indexes of the numbers summed up to target.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            sm = numbers[l] + numbers[r]
            if sm > target:
                r -= 1
            elif sm < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []