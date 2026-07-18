---
id: "981"
title: Time Based Key-Value Store
difficulty: 🟡 Medium
pattern: Binary Search
leetcode_url: https://leetcode.com/problems/time-based-key-value-store/description/
status: 🟨 Reviewing
time_complexity: O(1) for set(), O(logn) for get
space_complexity: O(m * n) - m is number of values, n is number of keys
date_created: 2026-07-18
---

## 🎯 Core Intuition
The set() and init() are trivial functions, I decided to use the dictionary where for key there is a list of tuples associated with value and timestamp. Therefore, set() function just adds the tuple to the dictionary for a certain key. At first, I did not understand the get() function meaning, but then I got that there can be stored different values for each timestamp and we need to return the most recent one to the given timestamp variable. So, the solution was to use the binary search and if the timestamp is higher that the middle one, then we can update the result to middle one and move the left pointer. This way, we can find the most recent one.


## 🚀 Optimal Solution

### Python Implementation
```python
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))
        print(self.d)

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        l = 0
        r = len(arr) - 1
        res = ""

        # [('one', 10), ('two', 20), ('three', 30)], timestamp = 15
        while l <= r:
            m = (l + r) // 2
            if timestamp < arr[m][1]:
                r = m - 1
            else:
                l = m + 1
                res = arr[m][0]
        return res
