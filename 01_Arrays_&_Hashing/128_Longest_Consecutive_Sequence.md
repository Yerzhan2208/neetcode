---
id: "128"
title: Longest Consecutive Sequence
difficulty: 🟡 Medium
pattern: Hash Set
leetcode_url: https://leetcode.com/problems/longest-consecutive-sequence/description/
status: 🟨 Reviewing
time_complexity: O(n) - the length of the given array
space_complexity: O(n) - the length of the given array
date_created: 2026-07-04
---

## 🎯 Core Intuition
I was struggling to find a way to start the solution. Of course, the bruteforce is obvious, but O(n) is harder so I took a hint. The hint gave me an idea to do the hash set and actually start counting the sequence from the back of it. This way for each number, I just checked if there is another number in set that is 1 smaller than the current.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        s = set(nums)
        res = 1
        mx = 1
        for i in nums:
            num = i
            if (num - 1) not in s:
                continue
            while (num - 1) in s:
                res += 1
                num -= 1
            if res > mx:
                mx = res
            res = 1
        return mx