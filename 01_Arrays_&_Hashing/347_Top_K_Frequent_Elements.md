---
id: "347"
title: Top K Frequent Elements
difficulty: 🟡 Medium
pattern: Arrays & Hashing
leetcode_url: https://leetcode.com/problems/top-k-frequent-elements/description/
status: 🟨 Reviewing
time_complexity: O(nlogn) - sorting the dictionary by values
space_complexity: O(n) - the size of dictionary is the number of elements (unique)
date_created: 2026-06-24
---

## 🎯 Core Intuition
To find the most frequent elements, we first need to know exactly how many times each element appears. By building a dictionary, we can then sort the unique numbers based on their frequency counts and slice off the top k results.

## 🚀 My Solution

### Python Implementation
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            d[i] = 1 + d.get(i, 0)

        return sorted(d, key=lambda x: d[x], reverse=True)[:k]
```
## 🚀 Optimal Solution (Bucket Sort)

### Python Implementation
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
```