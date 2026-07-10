---
id: "238"
title: Product of Array Except Self
difficulty: 🟡 Medium
pattern: Prefix & Suffix
leetcode_url: https://leetcode.com/problems/product-of-array-except-self/description/
status: 🟩 Mastered
time_complexity: O(n) - length of array
space_complexity: O(n)
date_created: 2026-06-25
---

## 🎯 Core Intuition
First thought is straightforward, the bruteforce and it definitely will take O(n2) time complexity, this solution is easy. The other idea is to identify the product of all numbers and then for each number in array we divide the product by this number, but the challenge occurred when 0 came up. Therefore, we need to deal with it.

After looking at the hint 3, I found out that the resulting array is the product of prefix and suffix arrays, where in prefix arrays product of previous numbers is stored and in the suffix array product of posterior numbers is stored.


## 🚀 O(n2) Solution

### Python Implementation
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            res.append(prod)
        return res
```
## 🚀 O(n) Solution

### Python Implementation
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        res = [0] * n

        prefix[0] = 1
        suffix[-1] = 1
        
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res
```
